from flask import Flask, render_template, send_file, make_response, url_for, Response,request,redirect

import pandas as pd
import io
import numpy as np
import requests
from scripts import center, gameRec, gameRec_modified, multi_game, multi_game_rating 



#Some preprocessing steps
#df = pd.read_excel("C:/Users/hdeok/Desktop/game_data/Game_ratings_PS4.xlsx")
df = pd.read_excel("Game_ratings_PS4.xlsx")
input_game = ''
df_1 = df['Users'].value_counts().rename_axis('Users').reset_index(name='counts')
df_1 = df_1[df_1['counts'] > 4]
df_2 = df.merge(df_1,how='inner', on ='Users') 
matrix = df_2.pivot_table(columns='Game_name', index='Users', values='user_rating', fill_value=0)
matrix_std = matrix.apply(center)
x = list(matrix.keys())
df_3 = pd.DataFrame(x , columns= ["Game_name"])


app = Flask(__name__)

@app.route('/')
#@app.route('/pandas', methods=("POST", "GET"))
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/pandas', methods = ['POST', 'GET'])
def GK():
    if request.method == 'GET':
        return f"The URL /pandas is accessed directly. Try going to '/form' to submit game name"
    if request.method == 'POST':
        form_data = request.form
        if str(form_data['Game_Name2'])=='' and str(form_data['Game_Name3'])=='':
            input_game = str(form_data['Game_Name'])
            df_4 = gameRec(input_game,matrix,df_2,matrix_std)
        elif str(form_data['Game_Name3'])=='':
            input_game1 = str(form_data['Game_Name'])
            input_game2 = str(form_data['Game_Name2'])
            df_4 = multi_game([input_game1,input_game2],df_3,matrix,df_2,matrix_std)
        else:
            input_game1 = str(form_data['Game_Name'])
            input_game2 = str(form_data['Game_Name2'])
            input_game3 = str(form_data['Game_Name3'])
            df_4 = multi_game([input_game1,input_game2,input_game3],df_3,matrix,df_2,matrix_std) 
    return render_template('pandas.html',PageTitle = "Pandas",table=[df_4.to_html(classes='data', index = False)], titles= df_4.columns.values)

@app.route('/advanced_search', methods=['GET', 'POST'])
def advanced_search():
    if request.method == 'POST':
        return redirect(url_for('form'))
    return render_template('advanced_form.html')

@app.route('/advanced_pandas', methods = ['POST', 'GET'])
# do stuff when the form is submitted
def GK_advanced():
    if request.method == 'GET':
        return f"The URL /advanced_pandas is accessed directly. Try going to '/advanced_form' to submit game name"
    if request.method == 'POST':   
        form_data = request.form
        if str(form_data['Game_Name2'])=='' and str(form_data['Game_Name3'])=='':
            input_game = str(form_data['Game_Name'])
            rating_game = int(str(form_data['rating']))
            game_dict = {input_game:rating_game}
            df_5 = multi_game_rating(game_dict,df_3,matrix,df_2,matrix_std)
        elif str(form_data['Game_Name3'])=='':
            input_game1 = str(form_data['Game_Name'])
            rating_game1 = int(str(form_data['rating']))
            input_game2 = str(form_data['Game_Name2'])
            rating_game2 = int(str(form_data['rating2']))
            game_dict = {input_game1:rating_game1,input_game2:rating_game2}
            df_5 = multi_game_rating(game_dict,df_3,matrix,df_2,matrix_std)
        else:
            input_game1 = str(form_data['Game_Name'])
            rating_game1 = int(str(form_data['rating']))
            input_game2 = str(form_data['Game_Name2'])
            rating_game2 = int(str(form_data['rating2']))
            input_game3 = str(form_data['Game_Name3'])
            rating_game3 = int(str(form_data['rating3']))
            game_dict = {input_game1:rating_game1,input_game2:rating_game2,input_game3:rating_game3}
            df_5 = multi_game_rating(game_dict,df_3,matrix,df_2,matrix_std)
    return render_template('advanced_pandas.html',PageTitle = "Pandas",table=[df_5.to_html(classes='data', index = False)], titles= df_5.columns.values)

if __name__ == '__main__':
    app.run(debug = True)
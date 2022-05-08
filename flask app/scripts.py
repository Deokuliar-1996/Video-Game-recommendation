import pandas as pd
import numpy as np
import math
#function to centre the data

def center(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row

def gameRec(g,matrix,df_test,matrix_std):
    dota = matrix_std[g]
#Calculate Pearson Sim with all other games.
    dota = matrix.corrwith(dota).dropna()
#create a DF to show how many times each game has been played and the mean time it has been played
    gameData = df_test.groupby('Game_name').agg({'user_rating': [np.size, np.mean]})
#Filter out any game played by less than n players.
    gameSim = gameData['user_rating']['size'] >= 0
    df = gameData[gameSim].join(pd.DataFrame(dota, columns=['similarity'])).reset_index()
    index = df.index
    entered_game = df["Game_name"] == g
    game_index = index[entered_game]
    df = df.drop(index=game_index)
    return df.sort_values(['similarity'], ascending=False)[:20]

#returns similarity scores for a given inpuut game. Will be used for multiple game input function
def gameRec_modified(g,matrix,df_test,matrix_std):
    dota = matrix_std[g]
#Calculate Pearson Sim with all other games.
    dota = matrix.corrwith(dota).dropna()
#create a DF to show how many times each game has been played and the mean time it has been played
    gameData = df_test.groupby('Game_name').agg({'user_rating': [np.size, np.mean]})
#Filter out any game played by less than n players.
    gameSim = gameData['user_rating']['size'] >= 0
    df = gameData[gameSim].join(pd.DataFrame(dota, columns=['similarity']))
    return df['similarity']


def multi_game(game_list,df_4,matrix,df_test,matrix_std):
    df_4['Total_similarity'] = 0
    for i in game_list:
        new_col = list(gameRec_modified(i,matrix,df_test,matrix_std))
        df_4[i] = new_col
        df_4['Total_similarity'] = df_4['Total_similarity'] + df_4[i]
        
    df_4['Total_similarity'] = df_4['Total_similarity']/len(game_list)
    
    return df_4[['Game_name','Total_similarity']].sort_values(['Total_similarity'], ascending=False)[len(game_list):20]


def multi_game_rating(game_dict,df_4,matrix,df_test,matrix_std):
    df_4['Total_similarity'] = 0
    rating_sum = 0
    games = []    
    for key in game_dict:
        if len(game_dict.keys())==1:
            if game_dict.get(key)==0:
                new_col = list(gameRec_modified(key,matrix,df_test,matrix_std))
                df_4[key] = new_col
                df_4['Total_similarity'] = df_4['Total_similarity'] + df_4[key]
                return df_4[['Game_name','Total_similarity']].sort_values(['Total_similarity'], ascending=True)[0:20]
            else:
                new_col = list(gameRec_modified(key,matrix,df_test,matrix_std))
                df_4[key] = new_col
                df_4['Total_similarity'] = df_4['Total_similarity'] + df_4[key]
                df_5 = df_4[df_4["Game_name"] != key]
                max_val = df_5['Total_similarity'].max()
                min_val = df_5['Total_similarity'].min()
                #print(max_val, min_val)
                adder=(max_val - min_val)/10
                max_range = min_val + adder*game_dict.get(key)
                df_out = df_5.loc[df_5['Total_similarity']<= max_range]
                return df_out[['Game_name','Total_similarity']].sort_values(['Total_similarity'], ascending=False)[0:20]
        else:
            new_col = list(gameRec_modified(key,matrix,df_test,matrix_std))
            df_4[key] = new_col
            df_4[key] = df_4[key]*((0.1)*game_dict.get(key))
            df_4['Total_similarity'] = df_4['Total_similarity'] + df_4[key]
            games.append(key)
            rating_sum+= game_dict.get(key)

    df_4['Total_similarity'] = df_4['Total_similarity']/len(game_dict)
    df_5 = df_4[~df_4["Game_name"].isin(games)]
    max_val = df_5['Total_similarity'].max()
    min_val = df_5['Total_similarity'].min()
    adder=(max_val - min_val)/10
    max_range = min_val + adder*(math.ceil(rating_sum/len(games)))
    df_6 = df_5.loc[df_5['Total_similarity']<= max_range]

    return df_6[['Game_name','Total_similarity']].sort_values(['Total_similarity'], ascending=False)[0:20]
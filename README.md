# Video-Game-recommendation
The video game industry is massive. In fact, it is bigger than the film and music industries combined, and only getting bigger.
Many well renowned companies are getting into the gaming industry. With the meta verse and web3 upcoming technologies , the gaming industry is primed to explode in the next few years. The changing demographics of gamers are perhaps the most intriguing trend in the video gaming business.The video game industry is heavily reliant on the trend of what is hot amongst gamers and it is an important metric for game developers on what games to create next.

This website recommends the user, video games based on their taste in video games. With movie recommendation systems being a common system, there is a need for good quality video game recommendation systems. This would help gamers choose what games to play based on their interests , thereby making it easier in their search for video games. Current popular video game recommendation engines don’t allow multi – game recommendations as well as more complex recommendation solutions.

Some of the advantages of this recommendation website over others on the internet is that:
1. It allows users to input upto 3 games and not only 1 or 2 games.
2. It allows for an advance search which takes into account the weightage of the game rating given by the users.

## Data Collection
1. The data we used for our project was scraped from https://www.metacritic.com/. We used the BeautifulSoup to and basic string operations which was later stored in a .csv file. 
2. We scraped 258,562 different reviews spanning 2716 games. Our data was filtered further to 58384 rows as only users with more than 4 reviews were considered. Our data contained 3 columns, the username, the video game and the rating of the game by the user.
3. Most of our time went getting relevant data as during scraping we did come across issues which were dealt with as needed. Once the data was collected, there was no need for any preprocessing as all those steps were part of the scraping script. 

**Basic Search**

![](https://github.com/Deokuliar-1996/Video-Game-recommendation/blob/main/flask%20app/Basic_recommender.gif)

**Advanced Search**

![](https://github.com/Deokuliar-1996/Video-Game-recommendation/blob/main/flask%20app/Advanced_recommender.gif)



There are two main ways in recommender systems for recommending products to users:
1. Content-Based Filtering -  This method is based on an item's description and a record of the user's preferences. 
2. Collaborative Filtering - This strategy is based on the notion that individuals who loved an item in the past would enjoy it again in the future.

<img width="600" height="300" alt="image" src="https://user-images.githubusercontent.com/46833935/168930125-6fdcb088-14c8-4138-8059-8438462b8ded.png">
We have used Collaborative Filtering as our methodology.

## Inferences and Learnings
We ran our video recommendation system on some test cases and below are a few interesting things we noticed.

1. Gamers tend to stick to a games in the same genre. For example if a user inputted action based games, most of the games recommended would be action games.
2. We noticed that there was a significant negative correlation between sports games and open-world action and survival games.
3. The ratings on sports games were much lesser than average rating of all games. 
4. The application uses data from one source(metacritic), and could cause performance bias as it might not be representative of the whole distribution.

## How to use
Make sure to install flask

Run app.py in the flask app folder. The entries of games on the website is case sensitive and hence use game_names.txt in the flask app folder to get the all the game names with the correct case. This is a bug we are working on to fix.
	
## Contributors
© Harsh Deokuliar © Sameer Mahajan


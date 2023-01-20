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




# How to use
Make sure to install flask

Run app.py in the flask app folder. The entries of games on the website is case sensitive and hence use game_names.txt in the flask app folder to get the all the game names with the correct case.
	


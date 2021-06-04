Project Description:
Sentimental analsyis for stock price prediction. In this project, we are trying to undertsand how human sentiments effect the stock price movement. For this project, we are downloading retweet from twitter and stocks intraday pricess using alpha advabtage api. 


Data collection Process:

1. exchanges.py - this fetches the list of all the stock exchanges
2. ticker.py - this fetches the list of stock symbols for each exchange 
3. stock_data.py - this fecthes the stock data for last two year for each stock symbol
4. Stock.py - This file fetches the retweets for different tickers. 

Data Exporation Process:

1. Download the retweet for various tickers
2. remove whitespaces, user names, website reference from the retweet to have a list of clean tweet.




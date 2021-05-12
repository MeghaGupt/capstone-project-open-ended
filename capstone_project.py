import pandas as pd

api_key = '9YBSFK0A7B24SLJ7'
#pip install alpha_vantage
#https://github.com/RomelTorres/alpha_vantage
#https://www.alphavantage.co/documentation/
#https://alpha-vantage.readthedocs.io/en/latest/#

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month2&apikey=demo





from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

ts = TimeSeries(key=api_key,  output_format='csv')##,  output_format='pandas')
#data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
csv_reader, meta_data = ts.get_intraday_extended(symbol='MSFT',interval='15min', slice='year1month1')#, adjusted=True)

#for row in csv_reader:
#    pprint(row)
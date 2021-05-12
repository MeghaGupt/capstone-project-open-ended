import pandas as pd
import requests
from configparser import ConfigParser
import glob
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import os



def read_config(filename='config.ini', section='alpha_vantage'):
    """ Read configuration file and return a dictionary object
    
    Args:
       filename: name of the configuration file
       section: section of database configuration
    
    Return: 
        a dictionary of database parameters

    Reference:
        https://www.mysqltutorial.org/python-connecting-mysql-databases/
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            config[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return config


if __name__ == '__main__':

    config = read_config()
    filename = config['file_name']
    api_key =  config['api_key']
    slices = config['slices'].split(",")

    print(slices)

    filenames = glob.glob(filename + "*.csv")
    ts = TimeSeries(key=api_key,  output_format='csv')



    for file in filenames:
        df = pd.read_csv(file)

        for index, row in df.iterrows():

            for slice in slices:
                csv_reader, meta_data = ts.get_intraday_extended(symbol=row['Code'],interval='1min', slice=slice)#, adjusted=True)
                df_stock = pd.DataFrame(csv_reader, index=None)
                file_name = 'data\stock_data_'+ row['Code'] + '_' +slice + ".csv"
                df_stock.to_csv(file_name, sep= ',', header= True)


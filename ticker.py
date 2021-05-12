import pandas as pd
import requests
from configparser import ConfigParser




def read_config(filename='config.ini', section='eodhistoricaldata'):
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
    exchanges = pd.read_csv(config['exchange_csv'])
    api_key =  config['api_key']


    for index, exchange in exchanges.head(1).iterrows():
        df = pd.DataFrame()
        url = "https://eodhistoricaldata.com/api/exchange-symbol-list/"+ exchange['Code'] + "?api_token= " + api_key + "&fmt=json"
        response = requests.get(url)
        df = pd.DataFrame(response.json())
        file_name = 'data\stock_symbol_'+ exchange['Code']
        df.to_csv("file_name", sep= ',', header= True)
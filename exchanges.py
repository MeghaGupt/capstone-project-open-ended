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



url = "https://eodhistoricaldata.com/api/exchanges-list/?api_token=" + read_config()['api_key'] + "&fmt=json"


#response = requests.get("https://eodhistoricaldata.com/api/exchanges-list/?api_token=609ab308c85079.79546813&fmt=json")

response = requests.get(url)


df = pd.DataFrame(response.json())

df.to_csv("data\exchanges.csv", sep= ',', header= True)
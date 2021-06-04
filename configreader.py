import pandas as pd
import requests
from configparser import ConfigParser



class ConfigReader:
        
        def read_config(self, filename='config.ini', section='eodhistoricaldata'):
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
            self.parser = ConfigParser()
            self.parser.read(filename)

            # get section, default to mysql
            config = {}
            if self.parser.has_section(section):
                items = self.parser.items(section)
                for item in items:
                    config[item[0]] = item[1]
            else:
                raise Exception('{0} not found in the {1} file'.format(section, filename))

            return config
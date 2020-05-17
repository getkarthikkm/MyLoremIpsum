""" A python script to query a Database """
import psycopg2
import os
import logging
import argparse
import pandas as pd
import os

basedir    = os.path.abspath(os.path.dirname(__file__))
print("##basedir ->{}".format(basedir))


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set environment variables
os.environ['API_HOST'] = 'localhost'
os.environ['API_DBNAME'] = 'dvdrental'
os.environ['API_USER'] = 'postgres'
os.environ['API_PASSWORD'] = 'postgres'


class Database(object):
    """A class to handle Database Connection"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """ A __new__ method to instantiate database connection """
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            print("##args ->{}".format(args))
            print("##kwargs ->{}".format(kwargs))
            db_config = {
                'dbname': os.getenv('API_DBNAME'),
                'host': os.getenv('API_HOST'),
                'password': os.getenv('API_PASSWORD'),
                'user': os.getenv('API_USER')
            }

            try:
                logging.info('connecting to Oracle database...')
                connection = Database._instance.connection = psycopg2.connect(**db_config)
                cursor = Database._instance.cursor = connection.cursor()
                cursor.execute('SELECT VERSION()')
                db_version = cursor.fetchone()

            except Exception as error:
                logging.error('Error: connection not established {}'.format(error))
                Database._instance = None

            else:
                logging.info('connection established\n{}'.format(db_version[0]))

        return cls._instance

    def __init__(self, *args, **kwargs):
        """ A __init__ method to initialize database connection and cursor """
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def select_query_to_csv(self, query, output_path=basedir):
        """
        A method to query a given sql from the Database connection
        :param query: query string
        :return:
        """
        try:
            result = pd.read_sql(query, self.connection)

            out_path = os.path.abspath(os.path.join(output_path, 'query_extract.csv'))
            print('out_path ->{}'.format(out_path))
            result.to_csv(out_path, index=False)

        except Exception as error:
            logging.error('error executing query "{}", error: {}'.format(query, error))
            return None
        else:
            logging.info("'{}' query executed successfully \n".format(query))
            return result

    def __del__(self):
        self.connection.close()
        self.cursor.close()

# import postgres_connector
#
# new_db = postgres_connector.Database(host='host', user='user', password='password')
# result = new_db.select_query_to_csv("Select * from customer_list", 'C:\Karthik_Scripts')
# print(result)
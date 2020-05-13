""" A python script to query a Database """
import psycopg2
import os
import logging
import argparse
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set environment variables
os.environ['API_HOST'] = 'localhost'
os.environ['API_DBNAME'] = 'dvdrental'
os.environ['API_USER'] = 'postgres'
os.environ['API_PASSWORD'] = 'postgres'


class Database(object):
    """A class to handle Database Connection"""
    _instance = None

    def __new__(cls):
        """ A __new__ method to instantiate database connection """
        if cls._instance is None:
            cls._instance = object.__new__(cls)
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

    def __init__(self):
        """ A __init__ method to initialize database connection and cursor """
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def query(self, query):
        """
        A method to query a given sql from the Database connection
        :param query: query string
        :return:
        """
        try:
            result = pd.read_sql(query, self.connection)
        except Exception as error:
            logging.error('error executing query "{}", error: {}'.format(query, error))
            return None
        else:
            logging.info("'{}' query executed successfully \n".format(query))
            return result

    def __del__(self):
        self.connection.close()
        self.cursor.close()


if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(description='Parse the SQL query')

    # Add the parameters
    parser.add_argument('sql_string', help="SQL as string", type=str)

    # Parse the Arguments
    args = parser.parse_args()
    my_sql = args.sql_string

    # Instantiate the Database
    db = Database()
    data = db.query(my_sql)

    logging.info('{} Output Dataframe \n'.format(data.info))
    # Write to a CSV file
    data.to_csv('post_indicator2.csv',index=False)

# To execute
# python db.py "Select * from film"

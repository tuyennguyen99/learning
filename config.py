import os
from urllib.parse import quote
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hellow-world-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or quote('@1995N89y12345')
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    logging.error(SQLALCHEMY_DATABASE_URI)
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitylearning1234'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'USkJOFLzmHAzHP06ek5g2GgO81kfUqJmlt4Bb3gy7S6LqXqTdSpIDdVowcNTElcmL6ZUlV7Zhprn+AStKzMNSQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

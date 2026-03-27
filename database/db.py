# import mysql.connector
# from config import DB_CONFIG

import os
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        port=int(os.getenv('MYSQL_PORT', 3306))
    )
    return connection
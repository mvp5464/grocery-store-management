import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv()
MYSQL_SECRET = os.getenv('MYSQL_SECRET')

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connect(
                    user='root', 
                    password=MYSQL_SECRET, 
                    database='mySchema',
                    host='127.0.0.1', 
                    port=3306
                )
    return __cnx
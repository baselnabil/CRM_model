import mysql.connector
from mysql.connector import Error

def connection_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='crm',
            user='crm',
            password='password',
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()  # Get some info about the server
            print(f"Connected to MySQL Server version {db_info}")
            return connection
    except Error as err:
        print(f"MySQL connection failed: {err}")
        return None

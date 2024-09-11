import tkinter as tk
import mysql.connector
from mysql.connector import Error


# def connection_db():
#     try:
#         connection= mysql.connector.connect(
#             host='localhost',
#             database='crm',
#             user='crm',
#             password='password'
#         ) 
#         if connection.is_connected():
#             return connection
#     except Error as err:
#         print(f'mysql connection failed {err}')
#         return None 

import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self):
        # Database connection parameters
        self.host = 'localhost'
        self.database = 'crm'
        self.user = 'crm'
        self.password = 'password'
        self.connection = None  # Store the connection here

    def connection_db(self):
        try:
            # Establish connection using instance variables
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print('Connection to MySQL established')
                return self.connection
        except Error as err:
            print(f'MySQL connection failed: {err}')
            return None

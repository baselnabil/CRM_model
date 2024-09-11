import tkinter as tk
import sqlalchemy 
import mysql.connector 
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='crm',
            user='basel',
            password = 'password'
        )
        if connection.is_connected():
            return connection
    except Error as err :
        print(f'Error connecting to my sql {err}')
    return None



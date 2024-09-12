import mysql.connector
from mysql.connector import Error
import pandas as pd 
class TRANSACTIONS:
    def __init__(self,connection_db):
        self.connection = connection_db


    def add_transaction(self,company_name , transacion_type , transaction_date , transaction_amount):
        try:
            cursor = self.connection.cursor()
            qurey = 'INSERT INTO transactions(company_name,\
                transaction_type,\
                transaction_date,\
                transaction_amount) VALUES (%s, %s,%s,%s )'
            cursor.execute(qurey,(company_name , transacion_type , transaction_date , transaction_amount))
            self.connection.commit()
        except Error as err :
            print(f"value inserting error {err}")
        finally:
            cursor.close()  

    def search_transaction(self, transaction_date_begin, transaction_date_end):
        try:
            cursor = self.connection.cursor()
            query = 'SELECT * FROM transactions WHERE transaction_date BETWEEN %s AND %s'
        
            # Execute the query with the date range
            cursor.execute(query, (transaction_date_begin, transaction_date_end))
        
            # Fetch all results from the query
            results = cursor.fetchall()
            return results  # Return the fetched results
        except Error as err:
            print(f"Error with searching: {err}")
        finally:
            if cursor :
                cursor.close()  # Close only the cursor, not the connection
        # Optionally close the connection here if you are sure no further operations will be performed
        # self.connection.close()


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
                return connection
        except Error as err:
            print(f'there is an error with connecting to database {err}')
    

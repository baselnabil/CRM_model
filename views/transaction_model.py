import mysql.connector
from mysql.connector import Error


class TRANSACTIONS:
    def __init__(self,connection_db):
        self.connection = connection_db


    def add_transaction(self,company_name , transacion_type , transaction_date , transaction_amount):
        try:
            cursor = self.connection.cursor()
            qurey = 'INSERT INTO transactions(company_name,\
                transaction_type,\
                transaction_date,\
                transaction_amount) VALUES (%s , %s ,%s,%s )'
            cursor.execute(qurey,(company_name , transacion_type , transaction_date , transaction_amount))
            self.connection.commit()
        except Error as err :
            print(f"value inserting error {err}")
        finally:
            cursor.close()
            self.connection.close()  # Close connection after each transaction

    def search_transaction(self,search_type ,company_name , transacion_type , transaction_date_begin , transaction_date_end ):
        try:
            cursor =self.connection.cursor()
            if search_type =='By Name':
                query = 'SELECT * FROM transactions WHERE company_name = %s'
                cursor.execute(query,(company_name))
            elif search_type =='BY Type':
                query='SELECT * FROM transactions WHERE transacion_type = %s'
                cursor.execute(query,(transacion_type))
            elif search_type=='By Date':
                query='SELECT * FROM transactions WHERE transaction_data BETWEEN %s AND %s '
                cursor.execute(query,(transaction_date_begin,transaction_date_end))
            self.connection.commit()
        except Error as err:
            print(f'error with searching {err}')
        finally:
            cursor.close()
            self.connection.close()  # Close connection after each transaction



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
 
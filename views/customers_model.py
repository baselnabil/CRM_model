import mysql.connector
from mysql.connector import Error

class CustomerModel:
    def __init__(self,connection_db):
        self.connection = connection_db

    def create_customer(self, name, company_name, email, address, phone):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO customers (name, company_name, email, address, phone)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, company_name, email, address, phone))
            self.connection.commit()
        except Exception as e:
            print(f"Error creating customer: {e}")
        finally:
            cursor.close()

    def search_customer(self, name):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM customers WHERE name = %s"
            cursor.execute(query, (name,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error searching for customer: {e}")
        finally:
            cursor.close()

    def delete_customer(self, customer_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM customers WHERE customer_id = %s"
            cursor.execute(query, (customer_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting customer: {e}")
        finally:
            cursor.close()
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
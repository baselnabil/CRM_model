from db_connection import DB
class CustomerModel(DB):
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

import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Aadidev@123",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

connection_instance=DbConnect()
connection_instance.get_connection()

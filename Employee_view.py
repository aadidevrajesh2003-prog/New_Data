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

class GymMemberManager(DbConnect):
    def get_object(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from member where i d= %s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None

connection_instance=DbConnect()
connection_instance.get_connection()


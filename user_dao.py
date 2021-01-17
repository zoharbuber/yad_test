import sqlite3
from yad2_query import select_user_name_query, insert_query_user_name, select_adv_key_per_user

class UserDao:
    def __init__(self):
        self.conn = sqlite3.connect('yad2_db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (id int,
                    user_name text,
                    password text,
                    adv_key text)
                ''')
        self.conn.commit()

    def get_user_name(self):
        self.cursor.execute(select_user_name_query)
        user = self.cursor.fetchall()
        self.conn.commit()
        return user

    def insert_user_name(self, users):
        for user in users:
            self.cursor.execute(insert_query_user_name, [user.user_name, user.password, user.adv_key])
            self.conn.commit()

    def get_streets(self):
        self.cursor.execute(select_adv_key_per_user)
        streets = self.cursor.fetchall()
        self.conn.commit()
        return streets


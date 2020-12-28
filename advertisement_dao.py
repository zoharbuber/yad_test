import sqlite3
from yad2_query import create_table, select_query, insert_query
from Advertisement import Advertisement


class AdvertisementDAO:
    def __init__(self):
        self.conn = sqlite3.connect('yad2_db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Advertisement (
            streets text,
            prices text,
            apartment_types text,
            cities text,
            areas text,
            secondary_areas text)
        ''')
        self.conn.commit()

    def insert_advertisements(self, advertisements):
        for advertisement in advertisements:
            self.cursor.execute(insert_query, [advertisement.price])
            self.conn.commit()


import sqlite3
from yad2_query import insert_query, select_query


class AdvertisementDAO:
    def __init__(self):
        self.conn = sqlite3.connect('yad2_db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Advertisement (
            streets text,
            prices int,
            apartment_types text,
            cities text,
            areas text,
            secondary_areas text)
        ''')
        self.conn.commit()

    def insert_advertisements(self, advertisements):
        for advertisement in advertisements:
            self.cursor.execute(insert_query, [advertisement.street, advertisement.price, advertisement.apartment_type, advertisement.city, advertisement.area, advertisement.secondary_area])
            self.conn.commit()


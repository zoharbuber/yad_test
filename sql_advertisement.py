import sqlite3
from yad2_query import create_table, select_query, insert_query
from advertisement import Advertisement


conn = sqlite3.connect('yad2_db')
cursor = conn.cursor()

cursor.execute(create_table)

conn.commit()

cursor.execute(insert_query)

conn.commit()

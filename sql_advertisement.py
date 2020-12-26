import sqlite3
from yad2_query import create_table, select_query, insert_query
from advertisement import Advertisement


class sql_queries:
    def __init__(self):
        self.adv_data = Advertisement()

    def run_query(self):
        conn = sqlite3.connect('yad2_db')
        cursor = conn.cursor()

        try:
            cursor.execute(create_table)
            conn.commit()
        except Exception as e:
            print('error is: %s' % e)

        try:
            cursor.execute(select_query)
            conn.commit()
        except Exception as e:
            print('error is: %s' % e)

        try:
            for price in self.adv_data.prices:
                cursor.execute(insert_query, price)
                conn.commit()
        except Exception as e:
            print('error is: %s' % e)


if __name__ == '__main__':
    sql = sql_queries()
    sql.run_query()

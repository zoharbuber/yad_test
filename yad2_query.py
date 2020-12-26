create_table = '''

CREATE TABLE IF NOT EXISTS Advertisement (
    streets text,
    prices text,
    apartment_types text,
    cities text,
    areas text,
    secondary_areas text)
'''

insert_query = '''
INSERT INTO Advertisement(streets, prices) values(?,?); 
'''


select_query = '''
SELECT * FROM Advertisement 
'''

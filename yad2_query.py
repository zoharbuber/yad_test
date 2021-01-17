insert_query = '''
INSERT INTO Advertisement(streets, prices, apartment_types, cities, areas, secondary_areas) values(?,?,?,?,?,?); 
'''


select_user_name_query = '''
SELECT user_name FROM Users
'''

insert_query_user_name = '''
INSERT INTO Users(user_name, password, adv_key) values(?,?,?); 
'''

select_adv_key_per_user = '''
SELECT streets FROM Advertisement
WHERE users.adv_key = users.adv_key
'''
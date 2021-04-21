import psycopg2
from config import config


connect_with_database = psycopg2.connect(
    host = 'localhost',
    database='pp2_torekeldi',
    user='postgres',
    password='Counter2727'
)
create_table = str("""
    CREATE TABLE accounts_22 (
        user_id serial PRIMARY KEY,
        first_name VARCHAR UNIQUE NOT NULL
    );
    """)

sql = 'select * from account_of_students'
insert_data = """insert into account_of_students(first_name,second_name, created_date) values('Torekeldi2', 'Niyazbek2', '20.04.2021');"""
update_data = "update account_of_students set created_date = '20.04.2021' where user_id = 1;"
quory_data = "select first_name, second_name from account_of_students"
drop_data = "delete from account_of_students where first_name='Torekeldi1';"


cursor = connect_with_database.cursor()
cursor.execute(create_table)
""" row = cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone() """

connect_with_database.commit()
cursor.close()
connect_with_database.close()
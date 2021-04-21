import psycopg2
from config import config
""" 
v Connecting to the PostgreSQL database server
v Creating new PostgreSQL tables in Python
v Inserting data into the PostgreSQL table in Python
v Updating data in the PostgreSQL table in Python
v Querying data from the PostgreSQL tables
v Deleting data from PostgreSQL tables in Python 
"""
commands = list()

def create_data_table():
    name_of_table = input("Input the name of the table: ")
    print("""Before you'll create table, we have some rules:
    Data types: 
    VARCHAR - just names, names with numbers, its can contain specific characters.
    INT - numbers
    DATE - date in Year-Month-Date format
    
    If its unique information - add in the end UNIQUE
    If each line will have this information, add at the end: NOT NULL
    If its not last column - add at the end comma
    If its last column - just press enter
    """)
    create_table = ("""
    CREATE TABLE {} (
    


    """).format(name_of_table)
    
    while True:
        k = str(input())
        create_table += k
        create_table += '\n'
        if k[-1] !=',': break
        
    create_table += ");"
    print(create_table)
    commands.append(create_table)
    actions()


def drop_data_table():
    name_of_table = input("Input the name of the table: ")
    selected_data = input("Write the name which you want to delete: ")
    drop_data = """delete from {} where first_name='{}';""".format(name_of_table, selected_data)
    commands.append(drop_data)
    actions()


def querying_data_table():
    name_of_table = input("Input the name of the table: ")
    selected_data = input("Enter the names of the tables you would like to know. Please write them in one line and separated by commas! ")
    quory_data = """select {} from {}""".format(selected_data, name_of_table)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(quory_data)
        row = cur.fetchone()
        while row is not None:
            print(*row)
            row = cur.fetchone()
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

def update_data_table():
    name_of_table = input("Input the name of the table: ")
    last_name_of_pupil = input("Input the old name of the Student: ")
    new_name_of_pupil = input("Input the new name of the Student: ")
    update_data = """update {} set first_name = '{}' where first_name = '{}';""".format(name_of_table, new_name_of_pupil, last_name_of_pupil)
    commands.append(update_data)
    actions()


def insert_data_table():
    name_of_table = input("Input the name of the table: ")
    #name_of_columns = input("Input the name of columns of the table: ")
    name_of_input = input("Input data which you want to insert. PLEASE use '' this symbols when you enter data and use commas. For example: '666', 'Tokesh'\n")
    insert_data = """insert into {} values({})""".format(name_of_table, name_of_input)
    commands.append(insert_data)
    actions()


def actions():    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()


start = input("""
    Hello! What did you want?
    1 <--- Creating new table
    2 <--- Inserting data into table
    3 <--- Updating data in the table
    4 <--- Querying data from the table
    5 <--- Deleting data from table
    """)
if start =='1': create_data_table()
elif start == '2': insert_data_table()
elif start == '3': update_data_table()
elif start == '4': querying_data_table()
elif start == '5': drop_data_table()


import psycopg2
from config import config
""" 
vv Connecting to the PostgreSQL database server
vv Creating new PostgreSQL tables in Python
vv Inserting data into the PostgreSQL table in Python
vv Updating data in the PostgreSQL table in Python
vv Querying data from the PostgreSQL tables
vv Deleting data from PostgreSQL tables in Python 
vv Not to restart everytime
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
    commands.append(create_table)
    actions()
    zxc = input("""Please choose variant here!
    1 <--- Creating new table
    2 <--- Inserting data into table
    3 <--- Updating data in the table
    4 <--- Querying data from the table
    5 <--- Deleting data from table
    6 <--- Exit from programm
    """)
    if zxc =='1': create_data_table()
    elif zxc == '2': insert_data_table()
    elif zxc == '3': update_data_table()
    elif zxc == '4': querying_data_table()
    elif zxc == '5': drop_data_table()
    elif zxc == '6': exit(0)



def drop_data_table():
    name_of_table = input("Input the name of the table: ")
    name_of_column = input("Write the name of column where you want to delete data: ")
    data_of_column = input("Input the data, which you want to delete: ")
    drop_data = """delete from {} where {}='{}'""".format(name_of_table, name_of_column, data_of_column)
    while True:
        add_condition = input("""Did you want to add condition?
        1 - YES
        2 - NO
        """)
        if add_condition == '2': break
        else: k = input("Add some conditions like: and role_name = '666': ")
        drop_data += k
    drop_data += ';'
    commands.append(drop_data)
    actions()
    zxc = input("""Please choose variant here!
    1 <--- Creating new table
    2 <--- Inserting data into table
    3 <--- Updating data in the table
    4 <--- Querying data from the table
    5 <--- Deleting data from table
    6 <--- Exit from programm
    """)
    if zxc =='1': create_data_table()
    elif zxc == '2': insert_data_table()
    elif zxc == '3': update_data_table()
    elif zxc == '4': querying_data_table()
    elif zxc == '5': drop_data_table()
    elif zxc == '6': exit(0)


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
    zxc = input("""Please choose variant here!
    1 <--- Creating new table
    2 <--- Inserting data into table
    3 <--- Updating data in the table
    4 <--- Querying data from the table
    5 <--- Deleting data from table
    6 <--- Exit from programm
    """)
    if zxc =='1': create_data_table()
    elif zxc == '2': insert_data_table()
    elif zxc == '3': update_data_table()
    elif zxc == '4': querying_data_table()
    elif zxc == '5': drop_data_table()
    elif zxc == '6': exit(0)

def update_data_table():
    print("To update data, we using this format: i want to change this DATA = new_data where ADDRESS==? ")
    name_of_table = input("Input the name of the table: ")
    update_name_data = input("Insert name of column where you want to update data: ")
    update_info_data = input("Insert the data what you want to update: ")
    address = input("Input the ADDRESS: ")
    address_data = input("Input the information of this ADDRESS: ")
    update_data = """update {} set {} = '{}' where {} = '{}'""".format(name_of_table, update_name_data, update_info_data, address, address_data)
    while True:
        add_condition = input("""Did you want to add condition?
        1 - YES
        2 - NO
        """)
        if add_condition == '2': break
        else: k = input("Add some conditions like: and role_name = '666': ")
        update_data += k
    update_data += ';'
    commands.append(update_data)
    actions()
    zxc = input("""Please choose variant here!
    1 <--- Creating new table
    2 <--- Inserting data into table
    3 <--- Updating data in the table
    4 <--- Querying data from the table
    5 <--- Deleting data from table
    6 <--- Exit from programm
    """)
    if zxc =='1': create_data_table()
    elif zxc == '2': insert_data_table()
    elif zxc == '3': update_data_table()
    elif zxc == '4': querying_data_table()
    elif zxc == '5': drop_data_table()
    elif zxc == '6': exit(0)

def insert_data_table():
    name_of_table = input("Input the name of the table: ")
    #name_of_columns = input("Input the name of columns of the table: ")
    name_of_input = input("Input data which you want to insert. PLEASE use '' this symbols when you enter data and use commas. For example: '666', 'Tokesh'\n")
    insert_data = """insert into {} values({})""".format(name_of_table, name_of_input)
    commands.append(insert_data)
    actions()
    zxc = input("""Please choose variant here!
    1 <--- Creating new table
    2 <--- Inserting data into table
    3 <--- Updating data in the table
    4 <--- Querying data from the table
    5 <--- Deleting data from table
    6 <--- Exit from programm
    """)
    if zxc =='1': create_data_table()
    elif zxc == '2': insert_data_table()
    elif zxc == '3': update_data_table()
    elif zxc == '4': querying_data_table()
    elif zxc == '5': drop_data_table()
    elif zxc == '6': exit(0)


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


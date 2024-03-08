from connection import create_connection
from sqlite3 import DatabaseError
from SQLCommands.commands_to_create_table import sql_commands

def create_table(connection, sql_query):
    """ Parent function to create table from a SQL query """
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query)
    except DatabaseError as dberr:
        print(dberr)

def create_all_tables():
    """ The function that is iterated and call parent function to create all tables """
    with create_connection() as connection:
        if connection is not None:
            for command in sql_commands:
                create_table(connection, command)
            print('All tables are created successfully')
        else:
            print("Connection is None")
            


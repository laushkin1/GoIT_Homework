from connection import create_connection
from sqlite3 import DatabaseError
from faker import Faker
from random import randint, choice
from SQLCommands.commands_to_create_data import sql_create


fake = Faker()
GROUPS = ['Group A', 'Group B', 'Group C']
SUBJECTS = ['Math', 'Physics', 'Chemistry', 'Biology',
            'English', 'History', 'Computer Science']
HOW_MANY_TEACHERS = 5
HOW_MANY_STUDENTS = 50

def create_data(connection, sql_query, params):
    """ Parent function to create data from a SQL query """
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, params)
    except DatabaseError as err:
        print(err)
        

def create_groups(connection, sql_query=sql_create[0]):
    for group in GROUPS:
        create_data(connection, sql_query, params=(group, ))
    

def create_students(connection, sql_query=sql_create[1]):
    for _ in range(HOW_MANY_STUDENTS):
        name = fake.name()
        group_id = randint(1, len(GROUPS))
        create_data(connection, sql_query, params=(name, group_id))
        
def create_teachers(connection, sql_query=sql_create[2]):
    for _ in range(HOW_MANY_TEACHERS):
        name = fake.name()
        create_data(connection, sql_query, params=(name, ))
        
def create_subjects(connection, sql_query=sql_create[3]):
    teacher_ids = list(range(1, 6))
    for subject in SUBJECTS:
        teacher_id = choice(teacher_ids)
        create_data(connection, sql_query, params=(subject, teacher_id))
        
def create_marks(connection, sql_query=sql_create[4]):
    for student_id in range(1, 50 + 1):
        for subject_id in range(1, len(SUBJECTS) + 1):
            mark = randint(1, 12)
            date = fake.date_this_year().strftime('%Y.%m.%d')
            create_data(connection, sql_query,
                         params=(student_id, subject_id, mark, date))
            
def create_all_data():
    """ A function that calls all functions """
    with create_connection() as connection:
        if connection is not None:
            create_groups(connection)
            create_students(connection)
            create_teachers(connection)
            create_subjects(connection)
            create_marks(connection)
            print('All data are created successfully')
        else:
            print("Connection is None")


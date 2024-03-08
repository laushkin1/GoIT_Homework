from sqlite3 import DatabaseError
from connection import create_connection
from insert_data import SUBJECTS, HOW_MANY_TEACHERS, GROUPS, HOW_MANY_STUDENTS
from random import choice

"""
    ALL_QUERY is a list with 10 .sql files, 
    there is no zero file, so the first query with index one, 
    the second with index two, etc.
"""
ALL_QUERY = [f'./SQL_Query/query_{num}.sql' for num in range(0, 10+1)]
TEACHERS_ID = [id for id in range(1, HOW_MANY_TEACHERS+1)]
GROUPS_ID = [id for id in range(1, len(GROUPS)+1)]  
STUDENTS_ID = [id for id in range(1, HOW_MANY_STUDENTS+1)]


def print_res_query(connection, sql_query, params):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, params)
        print(cursor.fetchall())
    except DatabaseError as err:
        print(err)


def make_query(num_of_query, params = []):
    with create_connection() as connection:
        if connection is not None:
            with open(ALL_QUERY[num_of_query], 'r') as query_file:
                query = query_file.read()
            print_res_query(connection, query, params)


def run_first_query():
    print('5 students with the highest average score in all subjects:')
    make_query(1)


def run_second_query(subject=choice(SUBJECTS)):
    if subject not in SUBJECTS:
        print('There is no such subject in the database')
    else:
        print(f'Student with the highest score in {subject}:')
        make_query(2, params=(subject, ))


def run_third_query(subject=choice(SUBJECTS)):
    if subject not in SUBJECTS:
        print('There is no such subject in the database')
    else:
        print(f'The highest score in {subject} in all groups:')
        make_query(3, params=(subject, ))


def run_fourth_query():
    print('Average score on the course:')
    make_query(4)


def run_fifth_query(teacher_id=choice(TEACHERS_ID)):
    if teacher_id not in TEACHERS_ID:
        print('There are no such teacher id in the database')
    else:
        print(f'The courses are taught by a teacher with id {teacher_id}:')
        make_query(5, params=(teacher_id, ))


def run_sixth_query(group_id=choice(GROUPS_ID)):
    if group_id not in GROUPS_ID:
        print('There are no such group id in the database')
    else:
        print(f'List of students in a group with id {group_id}:')
        make_query(6, params=(group_id, ))


def run_seventh_query(group_id=choice(GROUPS_ID), subject=choice(SUBJECTS)):
    if group_id not in GROUPS_ID or subject not in SUBJECTS:
        print('This group or subject is not in the database')
    else:
        print(f'Student grades in group with id {group_id} in {subject}:')
        make_query(7, params=(group_id, subject))


def run_eighth_query(teacher_id=choice(TEACHERS_ID)):
    if teacher_id not in TEACHERS_ID:
        print('There are no such teacher id in the database')
    else:
        print(f'The average grades given by a teacher in his/her subjects:')
        make_query(8, params=(teacher_id, ))


def run_ninth_query(student_id=choice(STUDENTS_ID)):
    if student_id not in STUDENTS_ID:
        print('There are no such student id in the database')
    else:
        print(f'List of courses attended by the student with id {student_id}')
        make_query(9, params=(student_id, ))


def run_tenth_query(student_id=choice(STUDENTS_ID), teacher_id=choice(TEACHERS_ID)):
    if student_id not in STUDENTS_ID or teacher_id not in TEACHERS_ID:
        print('This student or teacher id not in the database')
    else:
        print(f'List of courses taught by the teacher with id {teacher_id} to student with id {student_id}')
        make_query(10, params=(student_id, teacher_id))

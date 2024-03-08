from sqlalchemy import func
from database.db import session
from random import choice
from database.models import Student, Mark, Subject, Group, Teacher
from seed import SUBJECTS, HOW_MANY_TEACHERS, GROUPS, HOW_MANY_STUDENTS

TEACHERS_ID = [id for id in range(1, HOW_MANY_TEACHERS+1)]
STUDENTS_ID = [id for id in range(1, HOW_MANY_STUDENTS+1)]


def select_1():
    top_students = (
    session.query(Student.name, func.avg(Mark.mark).label('average_mark'))
    .join(Mark, Student.id == Mark.student_id)
    .group_by(Student.id)
    .order_by(func.avg(Mark.mark).desc())
    .limit(5)
    .all()
    )
    for student_name, average_mark in top_students:
        print(f'Student: {student_name}, Average Mark: {round(average_mark, 2)}')
    
    
def select_2(subject=choice(SUBJECTS)):
    if subject not in SUBJECTS:
        print('There is no such subject in the database')
    else:
        sub_query = (
            session.query(Student.id, func.avg(Mark.mark).label('average_mark'))
            .join(Mark, Student.id == Mark.student_id)
            .join(Subject, Mark.subject_id == Subject.id)
            .filter(Subject.name == subject)
            .group_by(Student.id)
            .subquery()
        )

        result = (
            session.query(Student, sub_query.c.average_mark)
            .join(sub_query, Student.id == sub_query.c.id)
            .order_by(sub_query.c.average_mark.desc())
            .first()
        )

        top_student, average_mark = result
        print(f'Top Student for {subject}: {top_student.name}, Average Mark: {round(average_mark)}')
    
    
def select_3(subject=choice(SUBJECTS)):
    if subject not in SUBJECTS:
        print('There is no such subject in the database')
    else:
        result = (
            session.query(Group.name.label('group_name'), func.avg(Mark.mark).label('average_mark'))
            .join(Student, Group.id == Student.group_id)
            .join(Mark, Student.id == Mark.student_id)
            .join(Subject, Mark.subject_id == Subject.id)
            .filter(Subject.name == subject)
            .group_by(Group.name)
            .all()
        )
        
        print(f'For {subject}:')
        for group_name, average_mark in result:
            print(f'For {group_name} average mark: {round(average_mark, 2)}')
    
    
def select_4():
    average_mark = session.query(func.avg(Mark.mark)).scalar()
    print(f'Average Mark Overall: {round(average_mark, 2)}')
    
    
def select_5(teacher_id=choice(TEACHERS_ID)):
    if teacher_id not in TEACHERS_ID:
        print('There are no such teacher in the database')
    else:
        courses = \
            session.query(Subject.name) \
            .join(Teacher) \
            .filter(Teacher.id == teacher_id) \
            .all()
            
        target_teacher = session.query(Teacher).filter_by(id=teacher_id).first()
        if courses:
            print(f"Courses taught by {target_teacher.name}:")
            for course in courses:
                print(course.name)
        else:
            print(f"This teacher {target_teacher.name} is a slacker, he has no subjects to teach")
        print()
        print(f"Teacher ID: {teacher_id}")
        
        
def select_6(group_name=choice(GROUPS)):
    if group_name not in GROUPS:
        print('There are no such group in the database')
    else:
        students_in_group = session.query(Student).join(Group).filter(Group.name == group_name).all()
        print(f"List of students in the {group_name}:")
        for student in students_in_group:
            print(student.name)
        
        
def select_7(group_name=choice(GROUPS), subject_name=choice(SUBJECTS)):
    if group_name not in GROUPS or subject_name not in SUBJECTS:
        print('This group or subject is not in the database')
    else:
        marks_in_group_subject = (
            session.query(Student.name, Mark.mark)
            .join(Group)
            .join(Mark)
            .join(Subject)
            .filter(Group.name == group_name)
            .filter(Subject.name == subject_name)
            .all()
        )

        print(f"Students' grades in the {group_name} in the subject {subject_name}:")
        for student_name, mark in marks_in_group_subject:
            print(f"{student_name}: {mark}")

    
def select_8(teacher_id=choice(TEACHERS_ID)):
    average_mark = (
        session.query(func.avg(Mark.mark))
        .join(Subject)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .scalar()
    )
    
    target_teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if average_mark is not None:
        print(f"Average grade point average of the teacher {target_teacher.name}: {round(average_mark, 2)}")
    else:
        print(f"This teacher {target_teacher.name} is a slacker, he has no subjects to teach")
    print()
    print(f"Teacher ID: {teacher_id}")
    
    
def select_9(student_id=choice(STUDENTS_ID)):
    if student_id not in STUDENTS_ID:
        print('There are no such student id in the database')
    else:
        courses_attended = (
            session.query(Subject.name)
            .join(Mark)
            .join(Student)
            .filter(Student.id == student_id)
            .distinct()
            .all()
        )
        
        target_student = session.query(Student).filter_by(id=student_id).first()
        print(f"List of courses attended by the student {target_student.name}:")
        for course in courses_attended:
            print(course.name)
        print()
        print(f"Student ID: {student_id}")
    
    
def select_10(teacher_id=choice(TEACHERS_ID), student_id=choice(STUDENTS_ID)):
    if student_id not in STUDENTS_ID or teacher_id not in TEACHERS_ID:
        print('This student or teacher id not in the database')
    else:
        courses_attended_by_student = (
            session.query(Subject.name)
            .join(Mark, Mark.subject_id == Subject.id)
            .join(Student, Student.id == Mark.student_id)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .filter(Student.id == student_id)
            .filter(Teacher.id == teacher_id)
            .distinct()
            .all()
        )
        
        target_student = session.query(Student).filter_by(id=student_id).first()
        target_teacher = session.query(Teacher).filter_by(id=teacher_id).first()
        print(f"A list of courses that student {target_student.name} takes and teacher {target_teacher.name} teaches:")
        for course in courses_attended_by_student:
            print(f"{course.name}")
        print()
        print(f"Teacher ID: {teacher_id}\nStudent ID: {student_id}")


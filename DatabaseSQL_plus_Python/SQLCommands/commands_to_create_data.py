create_gruops_data = """
        INSERT INTO groups (name) VALUES (?)
    """

create_students_data = """    
        INSERT INTO students (name, group_id) VALUES (?, ?)
    """
    
create_teachers_date = """
        INSERT INTO teachers (name) VALUES (?)
    """
    
create_subjects_data = """
        INSERT INTO subjects (name, teacher_id) VALUES (?, ?)
    """
    
create_marks_data = """
        INSERT INTO marks (student_id, subject_id, mark, date) VALUES (?, ?, ?, ?)
    """

sql_create = [
    create_gruops_data, 
    create_students_data,
    create_teachers_date,
    create_subjects_data,
    create_marks_data
]

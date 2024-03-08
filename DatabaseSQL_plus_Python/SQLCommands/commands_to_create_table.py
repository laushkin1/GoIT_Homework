sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    )
    """

sql_create_group_table = """
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """

sql_create_teacher_table = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """

sql_create_subject_table = """
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )
    """

sql_create_marks_table = """
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        mark INTEGER,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """
    
sql_commands = [
    sql_create_students_table,
    sql_create_group_table,
    sql_create_teacher_table,
    sql_create_subject_table,
    sql_create_marks_table
]

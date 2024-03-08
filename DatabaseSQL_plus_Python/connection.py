import sqlite3
from contextlib import contextmanager

DATABASE = "MyUniversityDB.db"


@contextmanager
def create_connection():
    """Create connection to sqlite3 database"""
    connection = None
    try:
        connection = sqlite3.connect(DATABASE)
        yield connection
        connection.commit()
    except Exception as exp:
        print(exp)
        connection.rollback()
    finally:
        connection.close()

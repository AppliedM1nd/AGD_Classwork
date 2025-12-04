import sqlite3

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

create_students_table = """
CREATE TABLE IF NOT EXISTS STUDENTS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);
    
"""

cursor.execute(create_students_table)

conn.close()
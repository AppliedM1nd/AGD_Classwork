import sqlite3
conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()
insert_query = """
INSERT INTO students (first_name, last_name, age,gender)
VALUES ('Chris','Marinov',16,'Male');
"""

cursor.execute(insert_query)
conn.commit()
conn.close()
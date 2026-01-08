import sqlite3
from faker import Faker
import random

fake = Faker('en_US')
parameterised_insert_query = """
INSERT INTO
    students (first_name, last_name, age, gender)
VALUES
    (?, ?, ?, ?);
"""

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

fake.random.seed(4321)
random.seed(4321)
for _ in range(1000):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11,18)
    gender = random.choice(('Male', 'Female'))
    cursor.execute(parameterised_insert_query, (f_name, l_name, age, gender))



update_query = """
UPDATE students
SET last_name = ?
WHERE id = 4;
"""
cursor.execute(update_query, ('Smith',))
conn.commit()

increment_age_query = """
UPDATE students
SET age = age + 1;
"""

cursor.execute(increment_age_query)
conn.commit()
conn.close()
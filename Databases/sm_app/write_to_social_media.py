import sqlite3

add_to_users = """
INSERT INTO
    users(name,age,gender,nationality)
VALUES
    ('James',25,'male','USA'),
    ('Leila',32,'female','France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike',40,'male','Denmark'),
    ('Elizabeth', 21, 'female', 'Canada')
;
"""

with sqlite3.connect('sm_app_sqlite') as conn:
    cursor = conn.cursor()
    cursor.execute(add_to_users)
    conn.commit()
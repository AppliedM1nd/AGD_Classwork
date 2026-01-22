import sqlite3


add_to_posts = """
INSERT INTO
    posts(title, description, user_id)
VALUES
    ('Test1','Cool',1),
    ('Cool thing','Wow',2),
    ('Cool thing 2','Cool',3),
    ('TV SHOW','Subscribe',4),
    ('Weather report','Like the post',4)
;
"""

with sqlite3.connect('sm_app.sqlite') as conn:
    cursor = conn.cursor()
    cursor.execute(add_to_posts)
    conn.commit()
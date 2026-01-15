import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("SELECT text FROM comments WHERE text LIKE '%?';")
texts = cursor.fetchall()
for text in texts:
    print(text[0])

cursor.execute("UPDATE users SET name = 'Lizzy' WHERE name = 'Elizabeth';")
conn.commit()

cursor.execute("""
SELECT users.name, count(posts.id)
FROM users
INNER JOIN posts ON users.id = posts.user_id
GROUP BY posts.id;
""")
posts = cursor.fetchall()
for user in posts:
    print(user[0], user[1])

cursor.execute("""
SELECT users.name, comments.text
FROM users
INNER JOIN comments ON users.id = comments.user_id
ORDER BY users.name;
""")
comments = cursor.fetchall()
for row in comments:
    print(row[0], row[1])

conn.close()

import sqlite3

conn = sqlite3.connect('people_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

cursor.execute('''
INSERT INTO people (name, age) 
VALUES ('Олег', 35), ('Егор', 33), ('Игорь', 32)
''')
conn.commit()


def get_user_by_id(user_id):
    cursor.execute('SELECT name, age FROM people WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    if user:
        name, age = user
        print(f'Пользователь: {name}, Возраст: {age}')
    else:
        print(f'Пользователь с ID {user_id} не найден.')



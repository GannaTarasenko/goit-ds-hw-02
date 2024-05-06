from sqlite3 import Error
import sqlite3
from faker import Faker
import random

"""Підключення до бази даних"""
conn = sqlite3.connect("test.db")

"""Створення курсора"""
cur = conn.cursor()

"""Ініціалізація Faker"""
fake = Faker()

"""Заповнення таблиці users"""
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))

"""Заповнення таблиці status"""
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (?)", (status,))

"""Заповнення таблиці tasks"""
for _ in range(20):
    title = fake.text(max_nb_chars=100)
    description = fake.text()
    status_id = random.randint(1, len(statuses))
    user_id = random.randint(1, 10)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
                (title, description, status_id, user_id))

"""Підтвердження змін та закриття з'єднання"""
conn.commit()
conn.close()

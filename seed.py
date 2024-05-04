from faker import Faker
import psycopg2
import random

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Створення курсора
cur = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Заповнення таблиці status
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.text(max_nb_chars=100)
    description = fake.text()
    status_id = random.randint(1, len(statuses))
    user_id = random.randint(1, 10)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

# Підтвердження змін та закриття з'єднання
conn.commit()
conn.close()

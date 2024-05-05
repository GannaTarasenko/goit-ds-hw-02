import sqlite3

def get_tasks_by_user(user_id):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
    tasks = cur.fetchall()
    conn.close()
    return tasks

def get_tasks_by_status(status):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = ?)", (status,))
    tasks = cur.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, new_status):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = ?) WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

def get_users_without_tasks():
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)")
    users = cur.fetchall()
    conn.close()
    return users

def add_task(title, description, status_id, user_id):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
                (title, description, status_id, user_id))
    conn.commit()
    conn.close()

def get_incomplete_tasks():
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')")
    incomplete_tasks = cur.fetchall()
    conn.close()
    return incomplete_tasks

def delete_task(task_id):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def find_users_by_email(email_domain):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email LIKE ?", ('%@' + email_domain,))
    users = cur.fetchall()
    conn.close()
    return users

def update_user_name(user_id, new_name):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET fullname = ? WHERE id = ?", (new_name, user_id))
    conn.commit()
    conn.close()

def get_task_count_by_status():
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT s.name, COUNT(t.id) FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name")
    task_counts = cur.fetchall()
    conn.close()
    return task_counts

def get_tasks_assigned_to_domain(email_domain):
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE ?", ('%@' + email_domain,))
    tasks = cur.fetchall()
    conn.close()
    return tasks

def get_tasks_without_description():
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE description IS NULL")
    tasks = cur.fetchall()
    conn.close()
    return tasks

def get_users_and_task_counts():
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()
    cur.execute("SELECT u.fullname, COUNT(t.id) FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.id")
    users_and_task_counts = cur.fetchall()
    conn.close()
    return users_and_task_counts

if __name__ == '__main__':
    # Приклади використання запитів:
    print("Завдання користувача з ID 3:", get_tasks_by_user(3))
    print("Завдання зі статусом 'new':", get_tasks_by_status('new'))
    # Інші запити також можна викликати тут

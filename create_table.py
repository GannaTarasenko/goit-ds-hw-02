from sqlite3 import Error

from connect import create_connection, database

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == '__main__':
    """Створення таблиці users"""
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id integer PRIMARY KEY,
     fullname VARCHAR(100),
     email VARCHAR(100) UNIQUE
);
    """
    """Створення таблиці status"""
    sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
     id integer PRIMARY KEY,
     name VARCHAR(50) UNIQUE
);
    """
    """Створення таблиці tasks"""
    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id integer PRIMARY KEY,
     name text NOT NULL,
     priority integer,
     project_id integer NOT NULL,
     status Boolean default False,
     begin_date text NOT NULL,
     end_date text NOT NULL,
     FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
						# create users table
            create_table(conn, sql_create_users_table)
						# create status table
            create_table(conn, sql_create_status_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")

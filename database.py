import sqlite3

# create database or if it does not exist, connect to it
conn = sqlite3.connect('habit_database.db')

# create cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE IF NOT EXISTS habit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_name text
            )""")


def insert_habit(habit_name):
    with conn:
        c.execute("INSERT INTO habit VALUES (NULL, :habit_name)", {'habit_name': habit_name})


def get_habits():
    c.execute("SELECT * FROM habit")
    return print(c.fetchall())


# insert some sample data
# c.execute("INSERT INTO habit VALUES (2, 'Cooking')")
c.execute("SELECT * FROM habit")

# print(c.fetchone())

# commit the current transaction
conn.commit()

# close the connection
# conn.close()

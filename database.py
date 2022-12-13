import sqlite3
from classes import Habit

# rules for functional programming or "pure functions":
#   1) same input gives same output
#   2) no side effects e.g. no print statements, but returns instead
#   3) no global variables

# create database or if it does not exist, connect to it
conn = sqlite3.connect('habit_database.db')

# create cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE IF NOT EXISTS habit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text
            )""")


def insert(habit: Habit):
    with conn:
        c.execute("INSERT INTO habit VALUES (NULL, :name)", {'name': habit.name})


def get():
    c.execute("SELECT * FROM habit")
    return c.fetchall()


# commit the current transaction
conn.commit()

# close the connection
#conn.close()

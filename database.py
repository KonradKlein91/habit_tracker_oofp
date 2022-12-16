import sqlite3
from classes import Habit

# rules for functional programming or "pure functions":
#   1) same input gives same output
#   2) no side effects e.g. no print statements, but returns instead
#   3) no global variables

# connect to database
conn = sqlite3.connect('habit_database.db')

# create cursor
c = conn.cursor()


# creates the database table
def create_db():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS habit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            created datetime,
            periodicity integer
            )""")


# inserts a habit into the database
def insert(habit: Habit):
    with conn:
        c.execute("INSERT INTO habit VALUES (NULL, :name, :created, :periodicity)",
                  {'name': habit.name,
                   'created': habit.created,
                   'periodicity': habit.periodicity}
                  )


# returns a list of all habits in the database
def get():
    with conn:
        c.execute("SELECT * FROM habit")
        return c.fetchall()


# drops the database table and closes the connection
def clear():
    with conn:
        c.execute("DROP TABLE habit")

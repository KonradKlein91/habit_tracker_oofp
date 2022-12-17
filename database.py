import sqlite3


def create_db():
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Create the table
    conn.execute('''CREATE TABLE IF NOT EXISTS habits
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             created DATETIME,
             name TEXT NOT NULL,
             frequency INTEGER,
             streak INTEGER,
             last_completed DATETIME
             );''')

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()


def clear_database():
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Clear the database
    conn.execute('''DROP TABLE habits''')

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()


def create_habit(created, name, frequency):
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Add the habit to the database
    conn.execute('''INSERT INTO habits (created, name, frequency) VALUES (?, ?, ?)''',
                 (created, name, frequency))

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()


def get_habits():
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Query the database for all habits
    cursor = conn.execute('''SELECT * FROM habits''')

    # Fetch the results
    habits = cursor.fetchall()

    # Close the connection to the database
    conn.close()

    return habits

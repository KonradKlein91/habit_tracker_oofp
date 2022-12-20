import sqlite3


def create_db():
    """
    This function creates the database and the habits table
    """
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Create the table
    conn.execute('''CREATE TABLE IF NOT EXISTS habits
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             created DATETIME,
             name TEXT NOT NULL,
             frequency INTEGER,
             streak INTEGER,
             last_completed SmallDateTime
             );''')

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()


def clear_database():
    """
    This function clears the database by deleting all rows in the habits table
    """
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Clear the database
    conn.execute('''DELETE FROM habits''')

    # Commit the changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()


def get_habits():
    """
    This function returns a list of all habits in the database
    """
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Query the database for all habits
    cursor = conn.execute('''SELECT * FROM habits''')

    # Fetch the results
    habits = cursor.fetchall()

    # Close the connection to the database
    conn.close()

    return habits

# TODO add a function to get the longest streak
# TODO add a function to get all habits with ongoing streaks

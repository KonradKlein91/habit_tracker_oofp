import datetime
import sqlite3


class Habit:
    """Habit class"""

    def __init__(self, name: str, frequency: int):
        self.created = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.name = name
        self.frequency = frequency
        self.streak = 0
        self.last_completed = None

    @classmethod
    def create(cls, name, frequency):
        # Connect to the database
        conn = sqlite3.connect('database.db')

        # Add the habit to the database
        conn.execute('''INSERT INTO habits (created, name, frequency, streak, last_completed) VALUES (?, ?, ?, ? ,?)''',
                     (datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'), name, frequency, 0, None))

        # Commit the changes to the database
        conn.commit()

        # Close the connection to the database
        conn.close()

        # Return a new Habit object
        return cls(name, frequency)

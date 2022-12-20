import datetime
import sqlite3


class Habit:
    """Habit class"""

    def __init__(self, name: str, frequency: int):
        """
        Constructor

        :param name: name of the habit
        :param frequency: periodicity of the habit in number of days
        """
        self.created = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.name = name
        self.frequency = frequency
        self.streak = 0
        self.last_completed = 0

    def complete(self):
        """
        This function marks a habit as completed

        :return: None
        """
        self.last_completed = datetime.datetime.now()
        if self.last_completed - self.last_completed.replace(hour=0, minute=0, second=0,
                                                             microsecond=0) <= datetime.timedelta(
            days=self.frequency - 1):
            self.streak += 1
        else:
            self.streak = 1

        # change date format to match the database
        self.last_completed = self.last_completed.strftime('%Y-%m-%d %H:%M:%S')

        # Connect to the database
        conn = sqlite3.connect('database.db')

        # Add the habit to the database
        conn.execute(
            f'''UPDATE habits SET 
                streak = {self.streak}, 
                last_completed = '{self.last_completed}' 
                WHERE name = '{self.name}';
            ''')

        # Commit the changes to the database
        conn.commit()

        # Close the connection to the database
        conn.close()

    @classmethod
    def create(cls, name, frequency):
        """
        This function creates a new habit

        :param name: name of the habit
        :param frequency: periodicity of the habit

        :return: None
        """
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

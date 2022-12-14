import datetime


class Habit:
    """Habit class"""
    habit_name: str

    def __init__(self, name: str):
        self.name = name
        self.created = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

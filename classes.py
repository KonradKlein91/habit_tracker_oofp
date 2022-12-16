import datetime


class Habit:
    """Habit class"""

    def __init__(self, name: str, periodicity: int):
        self.name = name
        self.created = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.periodicity = periodicity

import fire

import database


class Habit:

    def __init__(self):
        self.habit_name = ()
    def create_habit(self, habit_name):
        self.habit_name = habit_name
        database.insert_habit(self.habit_name)
        return print(f"Habit {self.habit_name} has been created and has been added to the database")


if __name__ == "__main__":
    fire.Fire(Habit)  # Call main function

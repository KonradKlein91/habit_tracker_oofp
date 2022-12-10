import fire

import database


class Habit:
    def __init__(self, habit_name):
        self.habit_name = habit_name

    def create_habit(self):
        database.insert_habit(self.habit_name)
        print(f"Habit {self.habit_name} has been created and has been added to the database")


hab_5 = Habit("Cooking")
hab_5.create_habit()
database.get_habits()


if __name__ == "__main__":
    fire.Fire()  # Call main function

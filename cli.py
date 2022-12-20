import click
import database as db
import classes as cl
import os
import pandas as pd
from tabulate import tabulate


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", required=True, prompt="give the name of the habit", help="habit name")
@click.option("--frequency", required=True, type=int, prompt="give the periodicity of the habit in number of days", help="interval in days")
def create_habit(name, frequency):
    """create a new habit"""

    # clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # check if the frequency is valid
    if frequency <= 0:
        print("The frequency must be a positive integer!")
        return

    # creates a new habit object
    cl.Habit.create(name, frequency)

    # prints a message to the user
    click.echo(f"--------------------------------------------------------------------------------")
    click.echo('Habit ' + '\033[31m' + f'{name}' + '\033[39m' + f' created with a frequency of {frequency} days')
    click.echo(f"--------------------------------------------------------------------------------")


@cli.command()
@click.option("--name", prompt="What is the name of the habit you want to mark as completed?", help="habit name")
def complete(name):
    """Mark a habit as completed"""
    # clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # get all habits from the database
    habits = db.get_habits()

    # setup a df to find the habit
    df = pd.DataFrame(habits, columns=['id', 'created', 'name', 'frequency', 'streak', 'last_completed'])

    # find the habit
    selected_habit = df.loc[df['name'] == name]

    # TODO add error handling if the habit is not found
    # TODO add case handling when two habits have the same name
    #  -> ask the user to select the habit or prevent the user from creating two habits with the same name
    # iterate over the habit and complete it
    for index, row in selected_habit.iterrows():
        habit = cl.Habit(row['name'], row['frequency'])
        cl.Habit.complete(habit)

        # prints a message to the user
        click.echo(f"--------------------------------------------------------------------------------")
        click.echo('Habit ' + '\033[31m' + f'{name}' + '\033[39m'
                   + ' has been marked as completed. You are currently on a '
                   + 'streak of ' + '\033[31m' + f'{habit.streak}' + '\033[39m' + ' period(s).'
                   )
        click.echo(f"--------------------------------------------------------------------------------")


@cli.command()
def get_habit_list() -> None:
    """
    get a list of all habits in the database and print it to the terminal
    """
    # clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # get the habits from the database and print them to the terminal
    print(tabulate(db.get_habits(),
                   headers=['id', 'created', 'name', 'frequency', 'streak', 'last_completed'],
                   tablefmt='psql'
                   )
          )


@cli.command()
def clear_db() -> None:
    """this deletes all rows in the database"""
    click.echo(f'The database has been cleared')
    db.clear_database()


@cli.command()
def create_db() -> None:
    """this connects and creates the database"""
    click.echo(f'The database has been created')
    db.create_db()


cli.add_command(create_habit)
cli.add_command(complete)
cli.add_command(get_habit_list)
cli.add_command(clear_db)
cli.add_command(create_db)

if __name__ == '__main__':
    cli()

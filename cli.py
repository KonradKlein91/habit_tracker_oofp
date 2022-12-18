import click
import database as db
import classes as cl
import os
from tabulate import tabulate


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt="give the name of the habit", help="habit name")
@click.option("--frequency", prompt="give the periodicity of the habit in number of days", help="interval in days")
def create_habit(name, frequency):
    """create a new habit"""

    # clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

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
    habits = db.get_habits()
    print(habits)
    for h in habits:
        if h[0] == name:
            habit = cl.Habit(h[0], h[1])
            habit.complete()
            click.echo(f'Habit "{name}" marked as completed')
            return
    click.echo(f'Habit "{name}" not found')


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

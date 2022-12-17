import click
import database as db
import classes as cl
import os
from tabulate import tabulate


@click.group()
def cli():
    pass


@cli.command()
@click.option("--habit_name", prompt="give the name of the habit", help="habit name")
@click.option("--habit_frequency", prompt="give the periodicity of the habit in number of days", help="interval in days")
def create_habit(habit_name, habit_frequency):
    """create a new habit"""

    # clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # creates a new habit object
    cl.Habit.create(habit_name, habit_frequency)

    # prints a message to the user
    click.echo(f"--------------------------------------------------------------------------------")
    click.echo('Habit ' + '\033[31m' + f'{habit_name}' + '\033[39m' + f' created with a frequency of {habit_frequency} days')
    click.echo(f"--------------------------------------------------------------------------------")



@cli.command()
def get_habit_list() -> None:
    """get a list of all habits in the database and print it"""
    click.echo(f'This is the list of all habits')
    print(tabulate(db.get(), headers=['id', 'name', 'created', 'periodicity'], tablefmt='psql'))


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
cli.add_command(get_habit_list)
cli.add_command(clear_db)
cli.add_command(create_db)

if __name__ == '__main__':
    cli()

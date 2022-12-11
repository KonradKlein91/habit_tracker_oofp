import click
from classes import Habit
import database as db


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt="give the name of the habit", help="habit name")
def create(name) -> None:
    """Create a new habit"""
    habit = Habit(name)
    db.insert_habit(habit)
    click.echo(f'Habit {name} created')


cli.add_command(create)

if __name__ == '__main__':
    cli()

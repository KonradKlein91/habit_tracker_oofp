import click
from classes import Habit
import database as db
from tabulate import tabulate


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt="give the name of the habit", help="habit name")
def create(name) -> None:
    """create a new habit"""
    habit = Habit(name)
    db.insert(habit)
    click.echo(f'Habit {name} created')


@cli.command()
def get_habit_list() -> None:
    """get a list of all habits in the database and print it"""
    click.echo(f'This is the list of all habits')
    print(tabulate(db.get(), headers=['id', 'name'], tablefmt='psql'))


@cli.command()
def clear_db() -> None:
    """this deletes all rows in the database"""
    click.echo(f'The database has been cleared')
    db.clear()

@cli.command()
def create_db() -> None:
    """this connects and creates the database"""
    click.echo(f'The database has been created')
    db.create_db()


cli.add_command(create)
cli.add_command(get_habit_list)
cli.add_command(clear_db)
cli.add_command(create_db)

if __name__ == '__main__':
    cli()

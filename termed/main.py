import click
from termed.util.service import Termed

@click.command()
@click.option("--pace", "-p", required=True)
@click.option("--session", "-s", required=True)
def main(pace, session):
    Termed(pace, session).run()


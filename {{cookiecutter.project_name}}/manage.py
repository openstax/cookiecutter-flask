import click
from datetime import datetime

from flask import current_app
from flask_security import utils

from {{cookiecutter.project_name}} import create_app
from {{cookiecutter.project_name}} import db

app = create_app()



@app.cli.command()
@click.confirmation_option(prompt='This will erase everything in the database. Do you want to continue?')
def reset_db():
    """Resets the database to the original state using alembic downgrade and upgrade commands"""
    from alembic.command import downgrade, upgrade
    from alembic.config import Config as AlembicConfig
    config = AlembicConfig('alembic.ini')
    downgrade(config, 'base')
    upgrade(config, 'head')
    print('Database has been reset')


if __name__ == '__main__':
    app.cli()

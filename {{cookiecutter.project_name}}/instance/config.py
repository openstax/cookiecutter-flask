import os
import uuid

from {{ cookiecutter.project_name }}.utils import make_database_url

# MAIN FLASK APPLICATION
FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
FLASK_APP = 'wsgi.py'
DEBUG = os.environ.get('FLASK_DEBUG', False)
SECRET_KEY = os.environ.get('SESSION_SECRET', str(uuid.uuid4()))

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', make_database_url())
SQLALCHEMY_TRACK_MODIFICATIONS = False

# HEROKU
# Heroku requires the SERVER_NAME to be set to the app name ex. myapp.herokuapp.com
SERVER_NAME = os.environ.get('FLASK_SERVER_NAME', None)
# Heroku needs this set to 'https' to set all connections to https
PREFERRED_URL_SCHEME = os.environ.get('FLASK_PREFERRED_URL_SCHEME', 'http')

from flask import Flask

from {{ cookiecutter.project_name }}.core import db
from {{ cookiecutter.project_name }}.home.views import home


def create_app(package_name, package_path, settings_override=None):
    """
    This function creates the application using the application factory pattern.
    Extensions and blueprints are then initialized onto the the application
    object.

    http://flask.pocoo.org/docs/0.11/patterns/appfactories/

    :param package_name: the name of the package
    :param package_path: the path of the package
    :param settings_override: override default settings via a python object
    :return: app: the main flask application object
    """
    app = Flask(package_name,
                instance_relative_config=True,
                template_folder='templates')
    app.config.from_pyfile('config.py', silent=True)

    if settings_override:
        app.config.from_object(settings_override)

    # Attach Flask Extensions
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(home, url_prefix="/")


    return app

# Flask Cookiecutter

Use this cookiecutter to create a Flask project structure that includes the use
of the [application factorypattern][app-factory] and [blueprints][blueprints].

## Getting Started

Download `cookiecutter` to a global python path

    $ pip install cookiecutter

In your project directory run

    $ cookiecutter https://github.com/openstax/cookiecutter-flask.git

Answer the prompts then `cd` into your newly created project directory.

Create a virtualenv
    
    $ make venv

Activate the virtualenv
    
    $ source venv/bin/activate

Run the flask web server

    $ flask run


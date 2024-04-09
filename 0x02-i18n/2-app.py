#!/usr/bin/env python3
""" Babel i18n module """
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Babel Configuration Class """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Function that renders a Basic Template for Babel Implementation"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """Function selecting a language translation to use for a request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()

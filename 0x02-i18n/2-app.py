#!/usr/bin/env python3

"""Configure Flask-Babel to support EN & FR"""

from flask import Flask, render_template, request

from flask_babel import Babel, get_locale

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """Get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """ Basic Flask App
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0000000', port=5000, debug=True)

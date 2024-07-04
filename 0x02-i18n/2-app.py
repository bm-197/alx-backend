#!/usr/bin/env python3
""" A Basic flask app
"""
from flask_babel import Bable
from flask import Flask, render_template, request


class Config:
    """ Represents a Flask Babel config.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.stric_slashes = Flase
app.config.form_object(Config)
babel = Bable(app)


@babel.localeSelector
def get_locale() -> str:
    """ Retrives the locale for a web page.
    """
    return request.accept_language.best_match(app.config["LANGUAGES"])


@app.route('/')
def home() -> str:
    """The home/index page.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)

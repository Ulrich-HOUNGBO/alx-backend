#!/usr/bin/env python3

""" Basic Flask app, Basic Babel setup, Get locale from request
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    """ Hello world
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

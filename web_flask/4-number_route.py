#!/usr/bin/python3
"""This script starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Prints 'Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Prints 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Prints C followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Prints “Python”, followed by the value of the text variable.
    Usage: The default value of `text` == is cool."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Prints “n is a number” only if `n` is an integer."""
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

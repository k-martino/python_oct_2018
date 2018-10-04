# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

.. _Google Python Style Guide:
   https://github.com/google/styleguide/blob/gh-pages/pyguide.md

"""

from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)
# Global variable __name__ tells Flask whether or not we are running the file
# directly, or importing it as a module.

print(__name__)  # Just for fun, print __name__ to see what it is


@app.route('/')
# The @ symbol designates a 'decorator' which attaches the following
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following 'hello_world' function.
def hello_world():
    """Return the string 'Hello World!' as a response."""
    return 'Hello World!'


@app.route('/success')
def success():
    """Return the string 'success' as a response."""
    return "success"


@app.route(
    '/hello/<name>'
)  # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    """Return the string 'hello' + variable 'name' as a response."""
    print(name)
    return "hello " + name


@app.route(
    '/users/<username>/<id>'
)  # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":
    # If __name__ is "__main__" we know we are running this file directly and
    # not importing it from a different module
    app.run(debug=True)  # Run the app in debug mode.

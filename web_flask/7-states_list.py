#!/usr/bin/python3
"""This script starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/states_list')
def states_list():
    """Displays an HTML page: (inside the tag <BODY>.) 
    <H1> tag: “States”
    <UL> tag: with the list of all State objects present in
    DBStorage sorted by name (A->Z)
    <LI> tag: description of one State: 
                    <state.id>: <B><state.name></B>
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

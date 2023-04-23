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


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page: (inside the tag <BODY>.) 
    <H1> tag: “States”
    <UL> tag: with the list of all State objects present in
    DBStorage sorted by name (A->Z)
        <LI> tag: description of one State: 
        <state.id>: <B><state.name></B>
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page: (inside the tag <BODY>.) 
    If a State object is found with this <id>:
        <H1> tag: “States”
        <H3> tag: “Cities”
        <UL> tag: with the list of all State objects present in
        DBStorage sorted by name (A->Z)
            <LI> tag: description of one City: 
        <city.id>: <B><city.name></B>
    Otherwise:
        <H1> tag: “Not found!”
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

import sqlite3
import json
import os

from flask import Flask, request, send_file, redirect, url_for
from connection.sqlite3_connection import Sqlite3Connection, sqlite3_call


app = Flask(__name__)


@app.route("/")
def main():
    index_path = os.path.join(app.static_folder, "index.html")
    return send_file(index_path)


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route("/run", methods=["POST", "GET"])
def run():
    """
    In this function the connection is open and closed with every call -> inefficient
    """
    path = "./database/student.db"
    query = ""

    database = Sqlite3Connection(path)
    database.open()

    # extract query parameters
    if request.method == "GET":
        query = request.args.get("query")
    elif request.method == "POST":
        query = request.form["query"]

    try:
        result = sqlite3_call(database, query)
        output = json.dumps(result)
    except sqlite3.Error as err:
        output = err.args[0]

    database.close()
    return output


if __name__ == "__main__":
    # Only for debugging while developing and running main.py (without docker):
    # -> choose a port higher than 1000 to avoid permission problems
    #app.run(host="0.0.0.0", port=5000, debug=True)
    # Port 80 configuration to run via docker-compose up
    app.run(host="0.0.0.0", port=80, debug=True)

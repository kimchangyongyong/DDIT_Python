from flask import Flask
from flask.globals import request
from flask.templating import render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, ChangYong!'


if __name__ == '__main__':
    app.run(debug=True)

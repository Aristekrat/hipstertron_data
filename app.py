from flask import Flask, jsonify, make_response, request, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import timedelta
from functools import update_wrapper
from flask.ext.cors import CORS


app = Flask(__name__)
# One of the simplest configurations. Exposes all resources matching /api/* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin.
CORS(app, resources='/*', headers='Content-Type')
app.config.from_object('config')
db = SQLAlchemy(app)
import routes

if __name__ == '__main__':
    app.run()
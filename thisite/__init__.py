#!/usr/bin/env python3

from flask import Flask

from thisite.nce import nce

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


app.register_blueprint(nce, url_prefix='/nce')


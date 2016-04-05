#!/usr/bin/env python3

from flask import Flask

from nce import nce

app = Flask(__name__)

app.register_blueprint(nce, url_prefix='/nce')

app.run(port=80, debug=True)

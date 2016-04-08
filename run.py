#!/usr/bin/env python3

from flask import Flask

from nce import nce
from nikaya import nikaya

app = Flask(__name__)

app.register_blueprint(nce, url_prefix='/nce')
app.register_blueprint(nikaya, url_prefix='/nikaya')

app.run(port=8088, debug=True)

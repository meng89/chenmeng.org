#!/usr/bin/env python3

from flask import Flask

from nce import nce
from sutta import sutta

app = Flask(__name__)

app.register_blueprint(nce, url_prefix='/nce')
app.register_blueprint(sutta, url_prefix='/sutta')

app.run(port=80, debug=True)

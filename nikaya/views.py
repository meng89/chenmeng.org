import os
import flask
from flask import render_template, flash, redirect, request
from flask_autoindex import AutoIndex


from . import nikaya

from .config import BOOK_DIR

AutoIndex(nikaya, browse_root=BOOK_DIR)

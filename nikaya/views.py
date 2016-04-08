import os
import flask
from flask import render_template, flash, redirect, request
from flask_autoindex import AutoIndex


from . import nikaya

from .config import BOOKS_DIR

AutoIndex(nikaya, browse_root=BOOKS_DIR)

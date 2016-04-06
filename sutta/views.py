import flask
from flask import render_template, flash, redirect, request


from . import sutta

from .config import SUTTA_BOOKS_DIR


@sutta.route('/')
@sutta.route('/index')
def index():
    return render_template('index.html')


@sutta.route('/download', methods=['POST'])
def download():
    print(request.form.get('right'))

    book = request.form.get('book')
    if book:
        return flask.send_from_directory(SUTTA_BOOKS_DIR,
                                         '{}.epub'.format(book),
                                         as_attachment=True)

import flask
from flask import render_template, flash, redirect, request


from . import nce

from .config import NCE_BOOKS_DIR


@nce.route('/')
@nce.route('/index')
def index():
    return render_template('index.html')


@nce.route('/download', methods=['POST'])
def download():
    print(request.form.get('right'))

    book = request.form.get('book')
    if book:
        return flask.send_from_directory(NCE_BOOKS_DIR,
                                         '{}.epub'.format(book),
                                         as_attachment=True)

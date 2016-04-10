import os
import sys

import flask
from flask import render_template, flash, redirect, request


from . import nce

from .config import BOOK_DIR


@nce.route('/')
@nce.route('/index')
def index():

    books = []

    for filename in sorted(os.listdir(BOOK_DIR)):

        full_path = os.path.join(BOOK_DIR, filename)

        book = {
            'filename': filename,
            'mtime': os.path.getmtime(full_path),
            'size': os.path.getsize(full_path)
        }

        books.append(book)

    return render_template('index.html', books=books)


@nce.route('/download', methods=['POST'])
def download():

    print(request.form.get('right'))

    filename = request.form.get('book')

    if filename:
        return flask.send_from_directory(BOOK_DIR, filename, as_attachment=True)

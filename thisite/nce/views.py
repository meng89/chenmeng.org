import os

import flask
from flask import render_template, request


from . import nce

from .config import BOOK_DIR


reasonable1 = [
    '已有实体书',
    '曾有实体书，后来书坏了，扔了'
]

reasonable2 = [
    '所处之地买不到实体书',
    '买不起实体书'
]


requirement = '复制给别人前，会确保别人有获得的合理性，并同样告知别人复制时也需尽到此义务'


books = []
for filename in sorted(os.listdir(BOOK_DIR)):
    full_path = os.path.join(BOOK_DIR, filename)
    book = {
        'filename': filename,
        'mtime': os.path.getmtime(full_path),
        'size': os.path.getsize(full_path)
    }
    books.append(book)


@nce.route('/')
def index():

    return render_template('index.html',
                           books=books,
                           reasonable1=reasonable1, reasonable2=reasonable2,
                           requirement=requirement
                           )


@nce.route('/download', methods=['POST'])
def download():

    selected_reasonable = request.form.get('reasonable')

    selected_book = request.form.get('book')

    selected_requirement = request.form.get('requirement')

    if selected_book in [_book['filename'] for _book in books] \
            and selected_reasonable in reasonable1 + reasonable2 \
            and selected_requirement == requirement:

        return flask.send_from_directory(BOOK_DIR, selected_book, as_attachment=True)
    else:
        return None, 403

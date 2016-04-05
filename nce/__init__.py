from flask import Blueprint

nce = Blueprint('nce', __name__,
                template_folder='templates',
                static_folder='static'
                )


from . import views


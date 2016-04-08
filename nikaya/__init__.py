from flask import Blueprint

nikaya = Blueprint('nikaya', __name__,
                   template_folder='templates',
                   static_folder='static'
                   )


from . import views

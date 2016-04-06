from flask import Blueprint

sutta = Blueprint('sutta', __name__,
                  template_folder='templates',
                  static_folder='static'
                  )


from . import views

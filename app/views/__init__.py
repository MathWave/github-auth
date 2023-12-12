from flask import render_template
from app import appbuilder

"""
    Define you Views here
"""


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


from .login import LoginView
from .access_token import AccessTokenView
from .get_user import GetUserView


appbuilder.add_view_no_menu(LoginView())
appbuilder.add_view_no_menu(AccessTokenView())
appbuilder.add_view_no_menu(GetUserView())

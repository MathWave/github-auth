from uuid import uuid4

from flask import request, abort
from flask_appbuilder import BaseView, expose

from app.models import InternalUser


class AccessTokenView(BaseView):
    route_base = "/login/oauth/access_token"

    @expose(methods=['POST'])
    def post(self):
        state = request.form['code']
        user = InternalUser.objects(state=state).first()
        if user is None:
            abort(404)
        access_token = str(uuid4())
        user.access_token = access_token
        user.save()
        return {
            'access_token': access_token
        }

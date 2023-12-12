import uuid

from flask import render_template, request, abort
from flask_appbuilder import BaseView, expose

from app import appbuilder
from app.models import InternalUser
from app.utils import hash_password


class GetUserView(BaseView):
    route_base = "/get_user"

    @expose(methods=['GET'])
    def get(self):
        token = str(request.authorization).split()[1]
        user = InternalUser.objects(access_token=token).first()
        if not user:
            abort(404)
        return {
            'username': user.username
        }, 200

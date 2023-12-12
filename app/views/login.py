import uuid

from flask import render_template, request, redirect
from flask_appbuilder import BaseView, expose

from app import appbuilder
from app.models import InternalUser
from app.utils import hash_password


class LoginView(BaseView):
    route_base = "/auth"

    @expose(methods=['POST'])
    def post(self):
        form = request.form
        username = form['username']
        password = form['password']
        user = InternalUser.objects(username=username).first()
        if not user:
            return redirect(request.url, code=302)
        password_hash = hash_password(password)
        if user.password_hash != password_hash:
            return redirect(request.url, code=302)
        user.state = request.args['state']
        user.save()
        query_string = '?'.join(request.url.split('?')[1:])
        return redirect(f'/oauth-authorized/self?code={user.state}&{query_string}', 302)

    @expose(methods=['GET'])
    def get(self):
        state = request.args['state']
        print(state)
        return render_template(
            'login.html',
            base_template=appbuilder.base_template,
            appbuilder=appbuilder,
            state=state,
        ), 200

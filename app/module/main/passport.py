from . import api
from flask.views import MethodView
from flask import render_template, redirect,request
from ...models.user import login as user_login


@api('/passport/login/')
class Login(MethodView):

    def get(self, id=None):
        return render_template("main/passport/login.html")

    def post(self):
        mobile = request.form.get('mobile', None)
        password = request.form.get('password', None)
        user_login(mobile, password)
        return redirect('/')

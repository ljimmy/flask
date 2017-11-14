from . import route
from ...models.user import User
from flask import json
from ...models import serialize

@route('/user/profile')
def profile():

    user = User.query.get(1)
    user.mobile = 222
    user.save()
    return json.dumps(serialize(user))

@route("/user/join")
def join():
    user = User(mobile=123456)
    user.save()

    return json.dumps(serialize(user))
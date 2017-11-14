
from flask import jsonify

from app.models.user import Session
from app.models import serialize

from . import route,auth


@route('/user/profile')
@auth
def profile():
    return jsonify(serialize(Session.user)), 201
    
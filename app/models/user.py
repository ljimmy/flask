import datetime
from sqlalchemy import Column
from sqlalchemy import SmallInteger, Integer
from sqlalchemy import String, Unicode, TIMESTAMP
from  werkzeug.security import generate_password_hash, check_password_hash
from . import Base

class User(Base):

    __tablename__ = 'user'

    id = Column('user_id', Integer, primary_key=True)
    mobile = Column(String(255), unique=True)
    nickname = Column(Unicode(255))
    avatar = Column(String(255))

    _password = Column('password', String(255))

    state = Column(SmallInteger, default=1)
    create_at = Column(TIMESTAMP, default=datetime.datetime.now())


    @property
    def keys(self):
        return [
            'user_id',
            'mobile',
            'nickname',
            'avatar',
            'state',
            'create_at'
        ]

    @property
    def user_id(self):
        return self.id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        if not self._password:
            return False
        return check_password_hash(self._password, password)

class Session(object):
    user = None
    token = None

    @classmethod
    def setUid(cls, uid):
        user = User.query.get(uid)
        if not user:
            return False
        if user.state != 1:
            return False
        Session.user = user
        return True




def login(mobile, password):
    user = User.query.filter_by(mobile=mobile).first()
    if not user:
        User.throw400('无效的用户名或密码')
    if not user.check_password(password):
        User.throw400('无效的用户名或密码')
    return user

def join(mobile, password):

    if not mobile:
        User.throw400("无效的手机号码")

    if not password:
        User.throw400('无效的密码')

    user = User(mobile=mobile, password=password)

    try:
        user.save()
    except Exception as e:
        User.throw500(e.args)
    return user

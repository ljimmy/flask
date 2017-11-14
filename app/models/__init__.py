import datetime
from flask_sqlalchemy import SQLAlchemy

from ..libs.error import (
    NotFound,
    BadRequest,
    ServerError
)

db = SQLAlchemy()

def convert(value):
    if isinstance(value, datetime.datetime):
        value = value.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(value, datetime.date):
        value = value.strftime('%Y-%m-%d')
    return value


def serialize(model, columns=None):
    if columns is None:
        if hasattr(model, 'keys'):
            columns = model.keys
        else:
            columns = [c.key for c in model.__table__.columns]
    return dict(
        (c, convert(getattr(model, c))) for c in columns
    )

class Base(db.Model):
    def __getitem__(self, key):
        return getattr(self, key)
    __abstract__ = True

    def save(self, throw=True):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            if throw:
                raise e


    @staticmethod
    def throw404(*args, **kwargs):
        raise NotFound(*args, **kwargs)

    @staticmethod
    def throw500(*args, **kwargs):
        raise ServerError(*args, **kwargs)

    @staticmethod
    def throw400(*args, **kwargs):
        raise BadRequest(*args, **kwargs)

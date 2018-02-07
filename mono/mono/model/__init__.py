from flask_sqlalchemy import SQLAlchemy
from flask import json as _json

db = SQLAlchemy()


class MyModel(object):


    # 获取类内部所有属性
    def get_attrs(self):
        attrs = []
        for i in vars(self).items():
            if not i[0].startswith("_"):
                attrs.append(i)
        return attrs

    def put(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    def save(self):
        try:
            self.put()
            self.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def __json__(self):
        # vars()  获取类内部属性
        keys = vars(self).keys()
        # print(keys)
        data = {}
        for key in keys:
            if not key.startswith('_'):
                data[key] = getattr(self, key)
        return data


class JsonEncoder(_json.JSONEncoder):

    def default(self, o):
        if isinstance(o, db.Model):
            return o.__json__()
        return _json.JSONEncoder.default(self, o)



















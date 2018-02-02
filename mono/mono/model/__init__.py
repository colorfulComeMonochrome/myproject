from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyModel(object):


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






























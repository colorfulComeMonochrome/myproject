from mono.model import db, MyModel

"""
    用户
        id
        用户名
        密码
        昵称
        邮箱
        手机
        收藏

"""


class User(db.Model, MyModel):
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    neckname = db.Column(db.String(32), nullable=False, default='JRs')
    email = db.Column(db.String(50))
    phone_num = db.Column(db.Integer)
    collect = db.Column(db.Text)


    @classmethod
    def get(cls, username):
        user = User.query.filter_by(username=username).first()
        return user













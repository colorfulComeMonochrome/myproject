from mono.model import db
import time

"""
评论
    id
    用户id
    电影id
    
    评论时间
    评论状态 (是否回复,已被删除)(0无回复 1有回复 2已删除)
    回复评论id

"""


class Discuss(db.Model):
    d_id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer)
    m_id = db.Column(db.Integer)

    create_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, default=0)
    reply_d_id = db.Column(db.Text)





















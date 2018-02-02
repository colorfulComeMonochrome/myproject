from mono.model import db, MyModel

"""
电影
    id
    电影名
    电影描述
    url
"""


class Movie(db.Model, MyModel):
    m_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(50), nullable=False)
    movie_desc = db.Column(db.Text)
    url = db.Column(db.String(200))























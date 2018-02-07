import os


class DefaultConfig(object):

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session 使用
    SECRET_KEY = '\xf9\xfb\xdfIb\xb4\x0f\xab\xf1\xc9P\x97\xc5\xd4X"\x8ag\xa8\xd0\xe8|8\xcc'
    DEBUG = True
    # 注册mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@localhost/mono'























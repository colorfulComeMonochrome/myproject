import os


class DefaultConfig(object):

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
    # 注册mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@localhost/mono'























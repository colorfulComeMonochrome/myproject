from flask import Flask
from flask_classy import FlaskView
from mono.model import db, JsonEncoder
from mono.config.default import DefaultConfig
import pymysql


def create_app():

    app = Flask(__name__)
    pymysql.install_as_MySQLdb()
    app.config.from_object(DefaultConfig)
    # 统一注册所有的api接口
    api_register(app)
    # Index.register(app)
    app.json_encoder = JsonEncoder
    # 注册db
    db.init_app(app)
    return app


# 统一注册所有的api接口,以后注册app就不需要写xxx.register(app)  只需要在函数中导入对应的类即可
def api_register(app):
    from mono.api.index import Index
    from mono.api.user import UserView
    from mono.api.movie import MovieView

    """以下是注册第一个api(Index)时写的注释
    
    # 此时的locals().values() 中既有Index类,也有传参进来的app
    print(locals())   # locals()返回值是一个字典,
                        {'Index': <class 'mono.api.index.Index'>, 'app': <Flask 'mono.app'>}
                        所以要取其中的Index对象需要取locals().values()   
                        否则遍历locals()获得的是字典的键,类型是字符串
    print(type(locals()))
    print(locals().values())
    """
    for view in locals().values():
        # 将不是FlaskView的类过滤掉(例如app)
        if type(view) == type and issubclass(view, FlaskView):
            # print(type(view))
            view.register(app)








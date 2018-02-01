from flask_script import Manager, Shell, Server
from mono.app import create_app
# 导入migrate(迁移)包 实现自动创建table
from flask_migrate import Migrate, MigrateCommand
from mono.app import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('runserver', Server('0.0.0.0', port=5000))

# 将orm 的相关指令命名为db   并传入迁移相关的指令
manager.add_command('db', MigrateCommand)


# 在初始化shell时将需要的模块导入,方便测试
def shell_make_context():
    from mono.model.movie import Movie
    from mono.model.user import User
    from mono.model.discuss import Discuss
    content = locals()
    content['app'] = app
    content['db'] = db
    # print(content)
    return content


# 为项目配置shell
manager.add_command('shell', Shell(make_context=shell_make_context))


if __name__ == '__main__':
    manager.run()








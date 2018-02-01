from flask_script import Manager, Shell, Server
from mono.app import create_app

manager = Manager(create_app())

manager.add_command('runserver', Server('0.0.0.0', port=5000))

manager.add_command('shell', Shell)




if __name__ == '__main__':
    manager.run()








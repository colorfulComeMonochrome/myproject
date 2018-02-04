from flask_classy import FlaskView, route
from flask import request, json, jsonify
from mono.model.user import User
from mono.api import ApiView


class UserView(ApiView):

    def all(self):
        m = User.query.first()
        return m

    @route('/register/', methods=['POST'])
    def u_register(self):
        # 参数在request.values里
        # print(request.values)

        username = request.values['username']
        passwd = request.values['password']

        user = User()
        user.username = username
        user.password = passwd
        user.save()
        # print(username)
        # print(passwd)
        return jsonify(user)

    @route('/login/')
    def login(self):
        print(request)
        print(request.args)
        return 'login'






















from flask_classy import FlaskView, route
from flask import request, json, jsonify, session
from mono.model.user import User
from mono.api import ApiView
from mono.tools.code import Code
from hashlib import md5

"""
API:
    登录：验证账号,密码  u_id存入session中
    注册：获取请求中的信息
    退出登录
    修改信息：
    查询用户：
"""


class UserView(ApiView):

    def all(self):
        m = User.query.first()
        return m

    @route('/register/', methods=['POST'])
    def u_register(self):
        # 在参数传入注册函数时，前端应验证账号是否存在
        # 参数在request.values里
        info = request.values

        user = User()
        user.username = info.get('username')
        user.password = info.get('password')
        user.neckname = info.get('neckname')
        user.email = info.get('email')
        user.phone_num = info.get('phone_num')
        user.save()
        session['username'] = user.username
        # print(session)
        return user

    @route('/login/', methods=['POST'])
    def login(self):
        info = request.values
        username = request.values['username']
        password = request.values['password']
        u = User.get(username)

        if not u:
            return Code.user_not_exist, info
        if not u.password == password:
            return Code.password_wrong, info

        # session['username'] = username
        # print(session['username'])
        # print(session.items())

        # 使用md5来对进行session加密
        hash_object = md5()
        hash_object.update(u.username.encode('utf-8'))
        u.token = hash_object.hexdigest()

        session['u_token'] = u.token
        print(session.items())
        return u

    # 测试能否正常get session的api
    @route('/getsession/')
    def get_session(self, u_token):
        print("-------------------")
        # print(session.get('username'))
        print(request.values['u_token'])
        if request.values.get('u_token'):
            return Code.token_not_found, "failed"
        # if request.values['u_token'] == 0:
        #     return Code.success, "OK"
        # return Code.get_session_failed, "OK"
        return Code.success, "OK"

    # get
    @route('/logout/')
    def logout(self):
        username = request.values['username']
        # print("================================", username)
        if session.get(username):
            session.pop('username')
            return Code.success, "ok"
        else:
            return Code.never_logged_in, "ok"

    # 修改信息
    def alter(self):
        pass

    # 查询用户
    @route('/find/')
    def find_user(self):
        pass
















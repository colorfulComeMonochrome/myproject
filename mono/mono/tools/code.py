from enum import Enum


class Code(Enum):

    # 成功
    success = 200

    # 账号不存在
    user_not_exist = 301

    # 密码错误
    password_wrong = 302

    # 未登录
    never_logged_in = 303

    # test_session_get
    get_session_failed = 304

    #
    token_not_found = 305



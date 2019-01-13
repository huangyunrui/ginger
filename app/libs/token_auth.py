# @File    : token_auth.py
# @Date    : 2019-01-13
# @Author  : rui
from collections import namedtuple

from flask import  current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])

@auth.verify_password
def verify_password(token, password):
    # token
    # HTTP 账号密码
    # herader key:value
    # key = Authorization
    # value = basic baseb4(账号:密码 )
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # request
        g.user = user_info
        return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # # request 视图函数
    # allow = is_in_scope(scope, request.endpoint)
    # if not allow:
    #     raise Forbidden()
    return User(uid, ac_type, scope)
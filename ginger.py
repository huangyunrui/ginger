# -*- coding: utf-8 -*-

# @File    : tes.py
# @Date    : 2019-01-12
# @Author  : rui
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException

__author__  = 'rui'

app = create_app()

#全局捕获异常
@app.errorhandler(Exception)
def fraeword_error(e):

    if isinstance(e,APIException):
        return e

    if isinstance(e,HTTPException):
        code = e.code
        msg = e.description
        err_code = 1007
        return  APIException(msg,code,err_code)
    else:
        return APIException()



if __name__ == '__main__':
    app.run(debug=True)
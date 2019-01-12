# -*- coding: utf-8 -*-

# @File    : tes.py
# @Date    : 2019-01-12
# @Author  : rui
from app.app import create_app

__author__  = 'rui'

app = create_app()

@app.route('/v1/user/get')
def get_uesr():

    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)
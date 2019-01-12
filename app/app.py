# -*- coding: utf-8 -*-

# @File    : tes.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import Flask

def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1

    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    #flask上下问容器
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    # 蓝图注册
    register_blueprints(app)

    register_plugin(app)
    return app;
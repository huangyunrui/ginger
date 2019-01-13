# -*- coding: utf-8 -*-

# @File    : forms.py
# @Date    : 2019-01-12
# @Author  : rui
from wtforms import  StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[
        DataRequired(message='不允许为空'),
        length(min=5, max=32)
    ])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])
    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e

        self.type.data = client



class  UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(message="password不满足规则"),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$',message="密码格式不对")
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22,message="长度为2-22个字符")])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(message='邮箱已存在！')


    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError(message='昵称已存在！')


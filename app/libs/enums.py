# -*- coding: utf-8 -*-

# @File    : enums.py
# @Date    : 2019-01-12
# @Author  : rui
from enum import Enum


class ClientTypeEnum(Enum):
    UESR_EMAIL = 100
    UESR_MOBILE = 100

    #小程序
    USER_MINA = 200
    #微信
    USER_WX = 201
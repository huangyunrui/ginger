# -*- coding: utf-8 -*-

# @File    : book.py
# @Date    : 2019-01-12
# @Author  : rui
from flask import Blueprint

from app.libs.redprint import Redprint

# book = Blueprint('book',__name__)
api = Redprint('book')

@api.route('', methods=['GET'])
def get_book():
    return 'book1'


@api.route('', methods=['POST'])
def create():
    return 'book1'
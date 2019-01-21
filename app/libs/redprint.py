# -*- coding: utf-8 -*-

# @File    : redprint.py
# @Date    : 2019-01-12
# @Author  : rui

class Redprint:

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, url, **options):
        def decorator(f):
            self.mound.append((f,url,options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + \
                       options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

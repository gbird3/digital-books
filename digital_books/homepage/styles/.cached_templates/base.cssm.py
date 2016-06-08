# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1465357662.9009297
_enable_loop = True
_template_filename = 'C:/Users/gregb/repos/digital-books/digital_books/homepage/styles/base.cssm'
_template_uri = 'base.cssm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('/*.navbar.transparent.navbar-default {\r\n   border-width: 0px;\r\n   -webkit-box-shadow: 0px 0px;\r\n   box-shadow: 0px 0px;\r\n   background-color: rgba(0,0,0,0.0);\r\n   background-image: -webkit-gradient(linear, 50.00% 0.00%, 50.00% 100.00%, color-stop( 0% , rgba(0,0,0,0.00)),color-stop( 100% , rgba(0,0,0,0.00)));\r\n   background-image: -webkit-linear-gradient(270deg,rgba(0,0,0,0.00) 0%,rgba(0,0,0,0.00) 100%);\r\n   background-image: linear-gradient(180deg,rgba(0,0,0,0.00) 0%,rgba(0,0,0,0.00) 100%);\r\n\r\n}*/\r\n\r\n#main-image {\r\n  background-image: url("')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/books.jpeg");\r\n  background-size: 100%;\r\n  background-repeat: no-repeat;\r\n}\r\n\r\n/*#main_menu {\r\n  color: white;\r\n}*/\r\n\r\n/*.nav.navbar-nav.navbar-right a {\r\n  color: white;\r\n}\r\n/**/\r\n.nav.navbar-nav a {\r\n  font-size: 18px;\r\n}\r\n\r\n/*.nav.navbar-nav.navbar-left a {\r\n  color: white;\r\n  font-size: 18px;\r\n}*/\r\n#logo {\r\n  color: #01A2A6;\r\n  font-size: 30px;\r\n  margin-top: -5px;\r\n}\r\n\r\n.right {\r\n  position: absolute;\r\n  right: 190px;\r\n}\r\n\r\n.green-color {\r\n  color: #01A2A6;\r\n}\r\n\r\n.dark {\r\n  color: #B1FF7E;\r\n}\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "base.cssm", "line_map": {"24": 13, "17": 0, "31": 25, "25": 13, "23": 1}, "filename": "C:/Users/gregb/repos/digital-books/digital_books/homepage/styles/base.cssm"}
__M_END_METADATA
"""

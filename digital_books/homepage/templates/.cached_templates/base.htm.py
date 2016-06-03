# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1464930952.8201027
_enable_loop = True
_template_filename = 'C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'main_menu', 'content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.js"></script>\r\n\t\t<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.1/jquery-ui.js"></script>\r\n\r\n\t\t<!-- Optional: Reflection -->\r\n\t\t<script type="text/javascript" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/reflection.js"></script>\r\n\r\n\t\t<!-- interpolate, depends on jQ 1.8.0+ -->\r\n\t\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.interpolate.min.js"></script>\r\n\r\n\t\t<!-- Coverflow -->\r\n\t\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.coverflow.js"></script>\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.touchSwipe.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/dist/semantic.min.js"></script>\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n    <!-- Favicon -->\r\n    <link rel="shortcut icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/" />\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/dist/semantic.min.css">\r\n  </head>\r\n  <body>\r\n\r\n    <div id="main_menu">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\r\n    </div> <!--main_menu-->\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Digital Bookshelf')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n          <div class="ui stackable menu">\r\n            <div class="item">\r\n              <i class="big book icon"></i>\r\n            </div>\r\n            <a class="item">Books</a>\r\n            <div class="right menu">\r\n              <div class="item">\r\n                <div class="ui icon input">\r\n                  <input type="text" placeholder="Search...">\r\n                  <i class="search link icon"></i>\r\n                </div>\r\n              </div>\r\n              <a class="ui item">\r\n                Sign In\r\n              </a>\r\n              <a class="ui item">\r\n                Sign Up\r\n              </a>\r\n            </div>\r\n        </div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 66, "68": 69, "69": 69, "70": 69, "76": 12, "112": 106, "17": 4, "82": 12, "19": 0, "88": 40, "94": 40, "33": 2, "34": 4, "100": 64, "39": 12, "40": 15, "41": 19, "42": 19, "43": 22, "44": 22, "45": 25, "46": 25, "47": 27, "48": 27, "49": 28, "50": 28, "51": 32, "52": 32, "53": 32, "54": 34, "55": 34, "56": 35, "57": 35, "106": 64, "62": 61}, "filename": "C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/base.htm", "source_encoding": "utf-8", "uri": "base.htm"}
__M_END_METADATA
"""

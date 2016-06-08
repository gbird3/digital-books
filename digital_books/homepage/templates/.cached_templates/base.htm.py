# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1465358650.0814364
_enable_loop = True
_template_filename = 'C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'main_menu', 'title']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js"></script>\r\n\t\t<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.1/jquery-ui.js"></script>\r\n    <!-- <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/semantic.min.js"></script> -->\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\r\n    <!-- Favicon -->\r\n    <link rel="shortcut icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/" />\r\n    <!-- <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/semantic.min.css"> -->\r\n  </head>\r\n  <body id="main-image">\r\n\r\n    <div id="main_menu">\r\n        ')
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


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n          <nav class="navbar navbar-default transparent white">\r\n            <div class="container-fluid">\r\n            <!-- Brand and toggle get grouped for better mobile display -->\r\n            <div class="navbar-header">\r\n              <a class="navbar-brand" href="#"><span id="logo" class="glyphicon glyphicon-book"></span></a>\r\n            </div>\r\n\r\n            <!-- Collect the nav links, forms, and other content for toggling -->\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n              <ul class="nav navbar-nav navbar-left">\r\n                <li><a href="#">Books<span class="sr-only">(current)</span></a></li>\r\n              </ul>\r\n              <form name="search" class="navbar-form right" role="search">\r\n                <div class="form-group">\r\n                  <input name="isearch" id="search-form" type="text" class="form-control hidden" placeholder="Search">\r\n                </div>\r\n                <button id="search" type="submit" class="btn btn-default"><span class="glyphicon glyphicon-search"></span></button>\r\n              </form>\r\n              <ul class="nav navbar-nav navbar-right">\r\n                <li><a href="#">Login</a></li>\r\n                <li class="dropdown">\r\n                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Signup <span class="caret"></span></a>\r\n                  <ul class="dropdown-menu">\r\n                    <li><a href="#">Action</a></li>\r\n                    <li><a href="#">Another action</a></li>\r\n                    <li><a href="#">Something else here</a></li>\r\n                    <li role="separator" class="divider"></li>\r\n                    <li><a href="#">Separated link</a></li>\r\n                  </ul>\r\n                </li>\r\n              </ul>\r\n            </div><!-- /.navbar-collapse -->\r\n            </div><!-- /.container-fluid -->\r\n          </nav>\r\n        ')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "base.htm", "line_map": {"64": 74, "65": 74, "66": 74, "72": 69, "108": 102, "78": 69, "17": 4, "19": 0, "84": 31, "90": 31, "96": 12, "33": 2, "34": 4, "102": 12, "39": 12, "40": 15, "41": 17, "42": 17, "43": 18, "44": 18, "45": 22, "46": 22, "47": 22, "48": 23, "49": 23, "50": 25, "51": 25, "52": 26, "53": 26, "58": 66, "63": 71}, "filename": "C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/base.htm"}
__M_END_METADATA
"""

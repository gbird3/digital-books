# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1465358650.062919
_enable_loop = True
_template_filename = 'C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="clearfix"></div>\r\n\r\n  <div class="container">\r\n    <div class="row">\r\n      <div class="col-sm-1"></div>\r\n      <div class="col-sm-10"><h1 id="action-call" class="text-center dark">An Online Bookshelf for Kids</h1></div>\r\n      <div class="col-sm-1"></div>\r\n    </div>\r\n    <br>\r\n    <div class="row">\r\n      <div class="col-sm-4"></div>\r\n      <div id="action-btn" class="col-sm-4"><button class="btn btn-info btn-lg">Go Read Books</button></div>\r\n      <div class="col-sm-4"></div>\r\n    </div>\r\n  </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "index.html", "line_map": {"35": 1, "52": 3, "40": 20, "58": 52, "28": 0, "46": 3}, "filename": "C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/index.html"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1464931612.2245088
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\t<h1 class="ui header">Digital Books</h1>\r\n\t\t<div class="photos">\r\n\t\t\t<img class="cover" data-name="Attic" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/attic.jpg"/>\r\n\t\t\t<img class="cover" data-name="Aurora Borealis" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/aurora.jpg"/>\r\n\t\t\t<img class="cover" data-name="Barbecued steak" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/barbecue.jpg"/>\r\n\t\t\t<img class="cover" data-name="Black swan" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/blackswan.jpg"/>\r\n\t\t\t<img class="cover" data-name="Chess" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/chess.jpg"/>\r\n\t\t\t<img class="cover" data-name="Fire" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/fire.jpg"/>\r\n\t\t\t<img class="cover" data-name="Keyboard" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/keyboard.jpg"/>\r\n\t\t\t<img class="cover" data-name="Locomotive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/locomotive.jpg"/>\r\n\t\t\t<img class="cover" data-name="Novo-Diveevo monastery" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/diveevo.jpg"/>\r\n\t\t\t<img class="cover" data-name="Person" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/person.jpg"/>\r\n\t\t\t<img class="cover" data-name="Rose" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/rose.jpg"/>\r\n\t\t\t<img class="cover" data-name="Seagull" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/seagull.jpg"/>\r\n\t\t\t<img class="cover" data-name="Solar power" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/demo/solarpower.jpg"/>\r\n\t\t</div>\r\n\t\t<div id="photos-info">\r\n\t\t\t<div id="photos-name"></div>\r\n\t\t</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 11, "65": 12, "66": 12, "67": 13, "68": 13, "69": 14, "70": 14, "71": 15, "72": 15, "73": 16, "74": 16, "75": 17, "76": 17, "77": 18, "78": 18, "79": 19, "80": 19, "86": 80, "28": 0, "36": 1, "41": 26, "47": 3, "54": 3, "55": 7, "56": 7, "57": 8, "58": 8, "59": 9, "60": 9, "61": 10, "62": 10, "63": 11}, "filename": "C:/Users/gregb/repos/digital-books/digital_books/homepage/templates/index.html", "source_encoding": "utf-8", "uri": "index.html"}
__M_END_METADATA
"""

# coding:utf-8
"""
Class : sublime.View
Methods : show_at_center(location)
Return Value : None
Description : Scroll the view to center on the location, which may be a <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-point">point</a> or <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>.
"""


import sublime
import sublime_plugin


class ViewShowAtCenterCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

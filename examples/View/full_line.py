# coding:utf-8
"""
Class : sublime.View
Methods : full_line(region)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : As line(), but the region includes the trailing newline character, if any.
"""


import sublime
import sublime_plugin


class ViewFullLineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

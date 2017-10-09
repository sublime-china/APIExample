# coding:utf-8
"""
Class : sublime.View
Methods : extract_scope(point)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Returns the extent of the syntax scope name assigned to the character at the given point.
"""


import sublime
import sublime_plugin


class ViewExtractScopeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime.View
Methods : scope_name(point)
Return Value : str
Description : Returns the syntax scope name assigned to the character at the given point.
"""


import sublime
import sublime_plugin


class ViewScopeNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

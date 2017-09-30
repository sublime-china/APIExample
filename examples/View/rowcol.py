# coding:utf-8
"""
Class : sublime.View
Methods : rowcol(point)
Return Value : (int, int)
Description : Calculates the 0-based line and column numbers of the point.
"""


import sublime
import sublime_plugin


class ViewRowcolCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

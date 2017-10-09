# coding:utf-8
"""
Class : sublime.View
Methods : line_endings()
Return Value : str
Description : Returns the line endings used by the current file.
"""


import sublime
import sublime_plugin


class ViewLineEndingsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

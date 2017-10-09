# coding:utf-8
"""
Class : sublime.View
Methods : set_line_endings(line_endings)
Return Value : None
Description : Sets the line endings that will be applied when next saving.
"""


import sublime
import sublime_plugin


class ViewSetLineEndingsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

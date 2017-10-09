# coding:utf-8
"""
Class : sublime.View
Methods : is_read_only()
Return Value : bool
Description : Returns True if the buffer may not be modified.
"""


import sublime
import sublime_plugin


class ViewIsReadOnlyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

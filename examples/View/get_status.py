# coding:utf-8
"""
Class : sublime.View
Methods : get_status(key)
Return Value : str
Description : Returns the previously assigned value associated with the key, if any.
"""


import sublime
import sublime_plugin


class ViewGetStatusCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

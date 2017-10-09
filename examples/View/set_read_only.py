# coding:utf-8
"""
Class : sublime.View
Methods : set_read_only(value)
Return Value : None
Description : Sets the read only property on the buffer.
"""


import sublime
import sublime_plugin


class ViewSetReadOnlyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

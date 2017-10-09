# coding:utf-8
"""
Class : sublime.View
Methods : insert(edit, point, string)
Return Value : int
Description : Inserts the given string in the buffer at the specified point. Returns the number of characters inserted: this may be different if tabs are being translated into spaces in the current buffer.
"""


import sublime
import sublime_plugin


class ViewInsertCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

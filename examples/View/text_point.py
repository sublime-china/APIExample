# coding:utf-8
"""
Class : sublime.View
Methods : text_point(row, col)
Return Value : int
Description : Calculates the character offset of the given, 0-based, row and col. Note that col is interpreted as the number of characters to advance past the beginning of the row.
"""


import sublime
import sublime_plugin


class ViewTextPointCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

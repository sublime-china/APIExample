# coding:utf-8
"""
Class : sublime.View
Methods : erase(edit, region)
Return Value : None
Description : Erases the contents of the region from the buffer.
"""


import sublime
import sublime_plugin


class ViewEraseCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

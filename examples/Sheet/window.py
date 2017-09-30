# coding:utf-8
"""
Class : sublime.Sheet
Methods : window()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Window">Window</a> <em>or</em> None
Description : Returns the window containing the sheet. May be None if the sheet has been closed.
"""


import sublime
import sublime_plugin


class SheetWindowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

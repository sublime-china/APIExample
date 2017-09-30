# coding:utf-8
"""
Class : sublime.Window
Methods : sheets()
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Sheet">Sheet</a>]
Description : Returns all open sheets in the window.
"""


import sublime
import sublime_plugin


class WindowSheetsCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

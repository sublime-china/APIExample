# coding:utf-8
"""
Class : sublime.Window
Methods : sheets_in_group(group)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Sheet">Sheet</a>]
Description : Returns all open sheets in the given group.
"""


import sublime
import sublime_plugin


class WindowSheetsInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

# coding:utf-8
"""
Class : sublime.Window
Methods : active_sheet()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Sheet">Sheet</a>
Description : Returns the currently focused sheet.
"""


import sublime
import sublime_plugin


class WindowActiveSheetCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

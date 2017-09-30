# coding:utf-8
"""
Class : sublime.Window
Methods : get_sheet_index(sheet)
Return Value : (int, int)
Description : Returns the group, and index within the group of the sheet. Returns -1 if not found.
"""


import sublime
import sublime_plugin


class WindowGetSheetIndexCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

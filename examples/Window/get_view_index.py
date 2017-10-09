# coding:utf-8
"""
Class : sublime.Window
Methods : get_view_index(view)
Return Value : (int, int)
Description : Returns the group, and index within the group of the view. Returns -1 if not found.
"""


import sublime
import sublime_plugin


class WindowGetViewIndexCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

# coding:utf-8
"""
Class : sublime.Window
Methods : get_tabs_visible()
Return Value : bool
Description : Returns True if tabs will be shown for open files.
"""


import sublime
import sublime_plugin


class WindowGetTabsVisibleCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

# coding:utf-8
"""
Class : sublime.Window
Methods : active_panel()
Return Value : str <em>or</em> None
Description : Returns the name of the currently open panel, or None if no panel is open. Will return built-in panel names (e.g. "console", "find", etc) in addition to output panels.
"""


import sublime
import sublime_plugin


class WindowActivePanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

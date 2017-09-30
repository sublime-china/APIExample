# coding:utf-8
"""
Class : sublime.Window
Methods : destroy_output_panel(name)
Return Value : None
Description : Destroys the named output panel, hiding it if currently open.
"""


import sublime
import sublime_plugin


class WindowDestroyOutputPanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

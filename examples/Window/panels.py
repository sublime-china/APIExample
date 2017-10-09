# coding:utf-8
"""
Class : sublime.Window
Methods : panels()
Return Value : [str]
Description : Returns a list of the names of all panels that have not been marked as unlisted. Includes certain built-in panels in addition to output panels.
"""


import sublime
import sublime_plugin


class WindowPanelsCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

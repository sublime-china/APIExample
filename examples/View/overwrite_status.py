# coding:utf-8
"""
Class : sublime.View
Methods : overwrite_status()
Return Value : bool
Description : Returns the overwrite status, which the user normally toggles via the insert key.
"""


import sublime
import sublime_plugin


class ViewOverwriteStatusCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

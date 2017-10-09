# coding:utf-8
"""
Class : sublime.View
Methods : set_status(key, value)
Return Value : None
Description : Adds the status key to the view. The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key. Setting the value to the empty string will clear the status.
"""


import sublime
import sublime_plugin


class ViewSetStatusCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

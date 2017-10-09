# coding:utf-8
"""
Class : sublime.Settings
Methods : add_on_change(key, on_change)
Return Value : None
Description : Register a callback to be run whenever a setting in this object is changed.
"""


import sublime
import sublime_plugin


class SettingsAddOnChangeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

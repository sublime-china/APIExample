# coding:utf-8
"""
Class : sublime.Settings
Methods : erase(name)
Return Value : None
Description : Removes the named setting. Does not remove it from any parent Settings.
"""


import sublime
import sublime_plugin


class SettingsEraseCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

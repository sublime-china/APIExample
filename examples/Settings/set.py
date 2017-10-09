# coding:utf-8
"""
Class : sublime.Settings
Methods : set(name, value)
Return Value : None
Description : Sets the named setting. Only primitive types, lists, and dicts are accepted.
"""


import sublime
import sublime_plugin


class SettingsSetCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

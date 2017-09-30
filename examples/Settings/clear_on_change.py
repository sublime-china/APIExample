# coding:utf-8
"""
Class : sublime.Settings
Methods : clear_on_change(key)
Return Value : None
Description : Remove all callbacks registered with the given key.
"""


import sublime
import sublime_plugin


class SettingsClearOnChangeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

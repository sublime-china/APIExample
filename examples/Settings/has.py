# coding:utf-8
"""
Class : sublime.Settings
Methods : has(name)
Return Value : bool
Description : Returns True iff the named option exists in this set of Settings or one of its parents.
"""


import sublime
import sublime_plugin


class SettingsHasCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

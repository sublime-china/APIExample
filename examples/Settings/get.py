# coding:utf-8
"""
Class : sublime.Settings
Methods : get(name, &lt;default&gt;)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-value">value</a>
Description : Returns the named setting, or default if it's not defined. If not passed, default will have a value of None.
"""


import sublime
import sublime_plugin


class SettingsGetCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

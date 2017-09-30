# coding:utf-8
"""
Class : sublime.View
Methods : settings()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Settings">Settings</a>
Description : Returns a reference to the view's settings object. Any changes to this settings object will be private to this view.
"""


import sublime
import sublime_plugin


class ViewSettingsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

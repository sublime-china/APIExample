# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : is_applicable(settings)
Return Value : bool
Description : A @classmethod that receives a <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Settings">Settings</a> object and should return a bool indicating if this class applies to a view with those settings
"""


import sublime
import sublime_plugin


class ViewEventListenerIsApplicableCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

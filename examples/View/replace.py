# coding:utf-8
"""
Class : sublime.View
Methods : replace(edit, region, string)
Return Value : None
Description : Replaces the contents of the region with the given string.
"""


import sublime
import sublime_plugin


class ViewReplaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

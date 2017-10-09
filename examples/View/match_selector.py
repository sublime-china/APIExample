# coding:utf-8
"""
Class : sublime.View
Methods : match_selector(point, selector)
Return Value : bool
Description : Checks the selector against the scope at the given point, returning a bool if they match.
"""


import sublime
import sublime_plugin


class ViewMatchSelectorCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

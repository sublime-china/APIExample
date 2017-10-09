# coding:utf-8
"""
Class : sublime.Selection
Methods : contains(region)
Return Value : bool
Description : Returns True iff the given region is a subset.
"""


import sublime
import sublime_plugin


class SelectionContainsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

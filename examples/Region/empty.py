# coding:utf-8
"""
Class : sublime.Region
Methods : empty()
Return Value : bool
Description : Returns True iff begin() == end().
"""


import sublime
import sublime_plugin


class RegionEmptyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

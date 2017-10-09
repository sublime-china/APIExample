# coding:utf-8
"""
Class : sublime.Region
Methods : intersects(region)
Return Value : bool
Description : Returns True iff self == region or both include one or more positions in common.
"""


import sublime
import sublime_plugin


class RegionIntersectsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

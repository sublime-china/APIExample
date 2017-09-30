# coding:utf-8
"""
Class : sublime.Region
Methods : size()
Return Value : int
Description : Returns the number of characters spanned by the region. Always &gt;= 0.
"""


import sublime
import sublime_plugin


class RegionSizeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

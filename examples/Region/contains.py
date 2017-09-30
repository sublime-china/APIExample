# coding:utf-8
"""
Class : sublime.Region
Methods : contains(point)
Return Value : bool
Description : Returns True iff begin() &lt;= point &lt;= end().
"""


import sublime
import sublime_plugin


class RegionContainsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

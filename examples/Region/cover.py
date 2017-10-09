# coding:utf-8
"""
Class : sublime.Region
Methods : cover(region)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Returns a Region spanning both this and the given regions.
"""


import sublime
import sublime_plugin


class RegionCoverCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

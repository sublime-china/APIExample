# coding:utf-8
"""
Class : sublime.Region
Methods : intersection(region)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Returns the set intersection of the two regions.
"""


import sublime
import sublime_plugin


class RegionIntersectionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

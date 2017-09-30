# coding:utf-8
"""
Class : sublime.View
Methods : lines(region)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>]
Description : Returns a list of lines (in sorted order) intersecting the region.
"""


import sublime
import sublime_plugin


class ViewLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

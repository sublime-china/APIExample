# coding:utf-8
"""
Class : sublime.View
Methods : split_by_newlines(region)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>]
Description : Splits the region up such that each region returned exists on exactly one line.
"""


import sublime
import sublime_plugin


class ViewSplitByNewlinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

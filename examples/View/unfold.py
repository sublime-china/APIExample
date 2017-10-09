# coding:utf-8
"""
Class : sublime.View
Methods : unfold([regions])
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>]
Description : Unfolds all text in the regions, returning the unfolded regions
"""


import sublime
import sublime_plugin


class ViewUnfoldCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

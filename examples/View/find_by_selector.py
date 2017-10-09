# coding:utf-8
"""
Class : sublime.View
Methods : find_by_selector(selector)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>]
Description : Finds all regions in the file matching the given selector, returning them as a list.
"""


import sublime
import sublime_plugin


class ViewFindBySelectorCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

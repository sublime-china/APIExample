# coding:utf-8
"""
Class : sublime.Selection
Methods : add(region)
Return Value : None
Description : Adds the given region. It will be merged with any intersecting regions already contained within the set.
"""


import sublime
import sublime_plugin


class SelectionAddCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

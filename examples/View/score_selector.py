# coding:utf-8
"""
Class : sublime.View
Methods : score_selector(point, selector)
Return Value : int
Description : Matches the selector against the scope at the given point, returning a score. A score of 0 means no match, above 0 means a match. Different selectors may be compared against the same scope: a higher score means the selector is a better match for the scope.
"""


import sublime
import sublime_plugin


class ViewScoreSelectorCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime
Methods : score_selector(scope, selector)
Return Value : int
Description : Matches the selector against the given scope, returning a score. A score of 0 means no match, above 0 means a match. Different selectors may be compared against the same scope: a higher score means the selector is a better match for the scope.
"""


import sublime
import sublime_plugin


class sublimeScoreSelectorCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

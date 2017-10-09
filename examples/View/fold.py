# coding:utf-8
"""
Class : sublime.View
Methods : fold(region)
Return Value : bool
Description : Folds the given region, returning False if it was already folded
"""


import sublime
import sublime_plugin


class ViewFoldCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

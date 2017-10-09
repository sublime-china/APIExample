# coding:utf-8
"""
Class : sublime.View
Methods : is_primary()
Return Value : bool
Description : If the view is the primary view into a file. Will only be False if the user has opened multiple views into a file.
"""


import sublime
import sublime_plugin


class ViewIsPrimaryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime.View
Methods : is_dirty()
Return Value : bool
Description : Returns True if there are any unsaved modifications to the buffer.
"""


import sublime
import sublime_plugin


class ViewIsDirtyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime.View
Methods : change_count()
Return Value : int
Description : Returns the current change count. Each time the buffer is modified, the change count is incremented. The change count can be used to determine if the buffer has changed since the last it was inspected.
"""


import sublime
import sublime_plugin


class ViewChangeCountCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

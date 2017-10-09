# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_selection_modified()
Return Value : None
Description : Called after the selection has been modified in the view.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnSelectionModifiedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

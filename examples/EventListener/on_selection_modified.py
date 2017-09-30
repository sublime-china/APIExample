# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_selection_modified(view)
Return Value : None
Description : Called after the selection has been modified in a view.
"""


import sublime
import sublime_plugin


class EventListenerOnSelectionModifiedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

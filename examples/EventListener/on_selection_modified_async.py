# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_selection_modified_async(view)
Return Value : None
Description : Called after the selection has been modified in a view. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnSelectionModifiedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

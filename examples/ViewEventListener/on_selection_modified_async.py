# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_selection_modified_async()
Return Value : None
Description : Called after the selection has been modified in the view. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnSelectionModifiedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

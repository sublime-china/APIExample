# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_modified_async()
Return Value : None
Description : Called after changes have been made to the view. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnModifiedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

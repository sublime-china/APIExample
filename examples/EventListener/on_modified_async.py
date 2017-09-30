# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_modified_async(view)
Return Value : None
Description : Called after changes have been made to a view. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnModifiedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

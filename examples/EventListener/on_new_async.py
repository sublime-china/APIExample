# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_new_async(view)
Return Value : None
Description : Called when a new buffer is created. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnNewAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

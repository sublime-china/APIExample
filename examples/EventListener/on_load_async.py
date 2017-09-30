# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_load_async(view)
Return Value : None
Description : Called when the file is finished loading. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnLoadAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

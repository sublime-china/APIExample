# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_deactivated_async(view)
Return Value : None
Description : Called when a view loses input focus. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnDeactivatedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

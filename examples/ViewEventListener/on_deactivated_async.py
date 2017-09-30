# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_deactivated_async()
Return Value : None
Description : Called when the view loses input focus. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnDeactivatedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_activated_async()
Return Value : None
Description : Called when the view gains input focus. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnActivatedAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

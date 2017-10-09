# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_clone_async(view)
Return Value : None
Description : Called when a view is cloned from an existing one. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnCloneAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

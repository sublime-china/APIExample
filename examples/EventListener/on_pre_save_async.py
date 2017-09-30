# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_pre_save_async(view)
Return Value : None
Description : Called just before a view is saved. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnPreSaveAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

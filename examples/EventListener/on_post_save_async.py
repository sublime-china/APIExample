# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_post_save_async(view)
Return Value : None
Description : Called after a view has been saved. Runs in a separate thread, and does not block the application.
"""


import sublime
import sublime_plugin


class EventListenerOnPostSaveAsyncCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_pre_close(view)
Return Value : None
Description : Called when a view is about to be closed. The view will still be in the window at this point.
"""


import sublime
import sublime_plugin


class EventListenerOnPreCloseCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

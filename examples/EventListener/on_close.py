# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_close(view)
Return Value : None
Description : Called when a view is closed (note, there may still be other views into the same buffer).
"""


import sublime
import sublime_plugin


class EventListenerOnCloseCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_new(view)
Return Value : None
Description : Called when a new buffer is created.
"""


import sublime
import sublime_plugin


class EventListenerOnNewCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

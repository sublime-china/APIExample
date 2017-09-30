# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_deactivated(view)
Return Value : None
Description : Called when a view loses input focus.
"""


import sublime
import sublime_plugin


class EventListenerOnDeactivatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

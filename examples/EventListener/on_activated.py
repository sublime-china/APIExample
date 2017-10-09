# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_activated(view)
Return Value : None
Description : Called when a view gains input focus.
"""


import sublime
import sublime_plugin


class EventListenerOnActivatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

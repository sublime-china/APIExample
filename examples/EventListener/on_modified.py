# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_modified(view)
Return Value : None
Description : Called after changes have been made to a view.
"""


import sublime
import sublime_plugin


class EventListenerOnModifiedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

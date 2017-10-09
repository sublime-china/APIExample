# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_clone(view)
Return Value : None
Description : Called when a view is cloned from an existing one.
"""


import sublime
import sublime_plugin


class EventListenerOnCloneCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_load(view)
Return Value : None
Description : Called when the file is finished loading.
"""


import sublime
import sublime_plugin


class EventListenerOnLoadCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

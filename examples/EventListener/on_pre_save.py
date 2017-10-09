# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_pre_save(view)
Return Value : None
Description : Called just before a view is saved.
"""


import sublime
import sublime_plugin


class EventListenerOnPreSaveCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_post_save(view)
Return Value : None
Description : Called after a view has been saved.
"""


import sublime
import sublime_plugin


class EventListenerOnPostSaveCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

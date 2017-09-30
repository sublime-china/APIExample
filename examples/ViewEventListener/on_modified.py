# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_modified()
Return Value : None
Description : Called after changes have been made to the view.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnModifiedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

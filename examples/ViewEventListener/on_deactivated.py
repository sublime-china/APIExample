# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_deactivated()
Return Value : None
Description : Called when the view loses input focus.
"""


import sublime
import sublime_plugin


class ViewEventListenerOnDeactivatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

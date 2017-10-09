# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_post_window_command(window, command_name, args)
Return Value : None
Description : Called after a window command has been executed.
"""


import sublime
import sublime_plugin


class EventListenerOnPostWindowCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

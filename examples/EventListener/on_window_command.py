# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_window_command(window, command_name, args)
Return Value : (str, dict)
Description : Called when a window command is issued. The listener may return a (command, arguments) tuple to rewrite the command, or None to run the command unmodified.
"""


import sublime
import sublime_plugin


class EventListenerOnWindowCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

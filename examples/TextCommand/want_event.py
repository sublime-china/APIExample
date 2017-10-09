# coding:utf-8
"""
Class : sublime_plugin.TextCommand
Methods : want_event()
Return Value : bool
Description : Return True to receive an event argument when the command is triggered by a mouse action. The event information allows commands to determine which portion of the view was clicked on. The default implementation returns False.
"""


import sublime
import sublime_plugin


class TextCommandWantEventCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

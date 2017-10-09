# coding:utf-8
"""
Class : sublime_plugin.TextCommand
Methods : is_visible(&lt;args&gt;)
Return Value : bool
Description : Returns True if the command should be shown in the menu at this time. The default implementation always returns True.
"""


import sublime
import sublime_plugin


class TextCommandIsVisibleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

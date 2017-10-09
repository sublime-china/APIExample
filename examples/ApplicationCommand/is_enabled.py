# coding:utf-8
"""
Class : sublime_plugin.ApplicationCommand
Methods : is_enabled(&lt;args&gt;)
Return Value : bool
Description : Returns True if the command is able to be run at this time. The default implementation simply always returns True.
"""


import sublime
import sublime_plugin


class ApplicationCommandIsEnabledCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime
Methods : log_commands(flag)
Return Value : None
Description : Controls command logging. If enabled, all commands run from key bindings and the menu will be logged to the console.
"""


import sublime
import sublime_plugin


class sublimeLogCommandsCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

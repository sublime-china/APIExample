# coding:utf-8
"""
Class : sublime
Methods : get_macro()
Return Value : [dict]
Description : Returns a list of the commands and args that compromise the currently recorded macro. Each dict will contain the keys command and args.
"""


import sublime
import sublime_plugin


class sublimeGetMacroCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

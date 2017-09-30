# coding:utf-8
"""
Class : sublime_plugin.ApplicationCommand
Methods : description(&lt;args&gt;)
Return Value : str
Description : Returns a description of the command with the given arguments. Used in the menu, if no caption is provided. Return None to get the default description.
"""


import sublime
import sublime_plugin


class ApplicationCommandDescriptionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

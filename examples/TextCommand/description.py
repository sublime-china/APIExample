# coding:utf-8
"""
Class : sublime_plugin.TextCommand
Methods : description(&lt;args&gt;)
Return Value : str
Description : Returns a description of the command with the given arguments. Used in the menus, and for Undo / Redo descriptions. Return None to get the default description.
"""


import sublime
import sublime_plugin


class TextCommandDescriptionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

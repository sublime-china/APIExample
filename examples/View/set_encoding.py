# coding:utf-8
"""
Class : sublime.View
Methods : set_encoding(encoding)
Return Value : None
Description : Applies a new encoding to the file. This encoding will be used the next time the file is saved.
"""


import sublime
import sublime_plugin


class ViewSetEncodingCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

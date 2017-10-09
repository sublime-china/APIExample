# coding:utf-8
"""
Class : sublime.View
Methods : symbols()
Return Value : [(<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>, str)]
Description : Extract all the symbols defined in the buffer.
"""


import sublime
import sublime_plugin


class ViewSymbolsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

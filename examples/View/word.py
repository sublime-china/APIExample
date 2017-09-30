# coding:utf-8
"""
Class : sublime.View
Methods : word(region)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Returns a modified copy of region such that it starts at the beginning of a word, and ends at the end of a word. Note that it may span several words.
"""


import sublime
import sublime_plugin


class ViewWordCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

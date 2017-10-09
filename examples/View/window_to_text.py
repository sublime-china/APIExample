# coding:utf-8
"""
Class : sublime.View
Methods : window_to_text(vector)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-point">point</a>
Description : Converts a window position to a text point
"""


import sublime
import sublime_plugin


class ViewWindowToTextCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

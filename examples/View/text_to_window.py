# coding:utf-8
"""
Class : sublime.View
Methods : text_to_window(point)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-vector">vector</a>
Description : Converts a text point to a window position
"""


import sublime
import sublime_plugin


class ViewTextToWindowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

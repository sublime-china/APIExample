# coding:utf-8
"""
Class : sublime.View
Methods : window()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Window">Window</a>
Description : Returns a reference to the window containing the view.
"""


import sublime
import sublime_plugin


class ViewWindowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

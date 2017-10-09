# coding:utf-8
"""
Class : sublime.Window
Methods : views()
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>]
Description : Returns all open views in the window.
"""


import sublime
import sublime_plugin


class WindowViewsCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

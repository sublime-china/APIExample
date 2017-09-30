# coding:utf-8
"""
Class : sublime.Window
Methods : views_in_group(group)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>]
Description : Returns all open views in the given group.
"""


import sublime
import sublime_plugin


class WindowViewsInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

# coding:utf-8
"""
Class : sublime.Window
Methods : active_view_in_group(group)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>
Description : Returns the currently edited view in the given group.
"""


import sublime
import sublime_plugin


class WindowActiveViewInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

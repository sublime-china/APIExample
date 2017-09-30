# coding:utf-8
"""
Class : sublime.Window
Methods : find_output_panel(name)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a> <em>or</em> None
Description : Returns the view associated with the named output panel, or None if the output panel does not exist.
"""


import sublime
import sublime_plugin


class WindowFindOutputPanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

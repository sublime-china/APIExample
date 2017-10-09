# coding:utf-8
"""
Class : sublime.View
Methods : visible_region()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Returns the currently visible area of the view.
"""


import sublime
import sublime_plugin


class ViewVisibleRegionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

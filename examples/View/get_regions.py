# coding:utf-8
"""
Class : sublime.View
Methods : get_regions(key)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>]
Description : Return the regions associated with the given key, if any
"""


import sublime
import sublime_plugin


class ViewGetRegionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

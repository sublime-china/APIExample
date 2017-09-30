# coding:utf-8
"""
Class : sublime.View
Methods : show(location, &lt;show_surrounds&gt;)
Return Value : None
Description : Scroll the view to show the given location, which may be a <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-point">point</a>, <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a> or <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Selection">Selection</a>.
"""


import sublime
import sublime_plugin


class ViewShowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

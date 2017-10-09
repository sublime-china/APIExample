# coding:utf-8
"""
Class : sublime.View
Methods : expand_by_class(region, classes, &lt;separators&gt;)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Expands region to the left and right, until each side lands on a location that matches classes. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
"""


import sublime
import sublime_plugin


class ViewExpandByClassCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

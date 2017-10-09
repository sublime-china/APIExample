# coding:utf-8
"""
Class : sublime.View
Methods : find_by_class(point, forward, classes, &lt;separators&gt;)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Finds the next location after point that matches the given classes. If forward is False, searches backwards instead of forwards. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
"""


import sublime
import sublime_plugin


class ViewFindByClassCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

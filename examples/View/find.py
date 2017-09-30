# coding:utf-8
"""
Class : sublime.View
Methods : find(pattern, start_point, &lt;flags&gt;)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>
Description : Returns the first region matching the regex pattern, starting from start_point, or None if it can't be found. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together.
"""


import sublime
import sublime_plugin


class ViewFindCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

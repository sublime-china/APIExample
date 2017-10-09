# coding:utf-8
"""
Class : sublime.View
Methods : find_all(pattern, &lt;flags&gt;, &lt;format&gt;, &lt;extractions&gt;)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Region">Region</a>]
Description : Returns all (non-overlapping) regions matching the regex pattern. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together. If a format string is given, then all matches will be formatted with the formatted string and placed into the extractions list.
"""


import sublime
import sublime_plugin


class ViewFindAllCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

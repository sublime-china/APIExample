# coding:utf-8
"""
Class : sublime.View
Methods : run_command(string, &lt;args&gt;)
Return Value : None
Description : Runs the named <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.TextCommand">TextCommand</a> with the (optional) given args.
"""


import sublime
import sublime_plugin


class ViewRunCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

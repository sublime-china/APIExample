# coding:utf-8
"""
Class : sublime.Window
Methods : run_command(string, &lt;args&gt;)
Return Value : None
Description : Runs the named <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.WindowCommand">WindowCommand</a> with the (optional) given args. This method is able to run any sort of command, dispatching the command via input focus.
"""


import sublime
import sublime_plugin


class WindowRunCommandCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

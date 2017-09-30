# coding:utf-8
"""
Class : sublime
Methods : run_command(string, &lt;args&gt;)
Return Value : None
Description : Runs the named <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime_plugin.ApplicationCommand">ApplicationCommand</a> with the (optional) given args.
"""


import sublime
import sublime_plugin


class sublimeRunCommandCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

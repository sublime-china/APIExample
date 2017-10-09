# coding:utf-8
"""
Class : sublime.Window
Methods : find_open_file(file_name)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>
Description : Finds the named file in the list of open files, and returns the corresponding View, or None if no such file is open.
"""


import sublime
import sublime_plugin


class WindowFindOpenFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

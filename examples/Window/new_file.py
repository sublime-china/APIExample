# coding:utf-8
"""
Class : sublime.Window
Methods : new_file()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>
Description : Creates a new file. The returned view will be empty, and its is_loaded() method will return True.
"""


import sublime
import sublime_plugin


class WindowNewFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

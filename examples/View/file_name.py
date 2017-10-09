# coding:utf-8
"""
Class : sublime.View
Methods : file_name()
Return Value : str
Description : The full name file the file associated with the buffer, or None if it doesn't exist on disk.
"""


import sublime
import sublime_plugin


class ViewFileNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('==> Test file name')

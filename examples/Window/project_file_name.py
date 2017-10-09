# coding:utf-8
"""
Class : sublime.Window
Methods : project_file_name()
Return Value : str
Description : Returns name of the currently opened project file, if any.
"""


import sublime
import sublime_plugin


class WindowProjectFileNameCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

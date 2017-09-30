# coding:utf-8
"""
Class : sublime.Window
Methods : project_data()
Return Value : dict
Description : Returns the project data associated with the current window. The data is in the same format as the contents of a <span class="file">.sublime-project</span> file.
"""


import sublime
import sublime_plugin


class WindowProjectDataCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

# coding:utf-8
"""
Class : sublime.Window
Methods : set_project_data(data)
Return Value : None
Description : Updates the project data associated with the current window. If the window is associated with a <span class="file">.sublime-project</span> file, the project file will be updated on disk, otherwise the window will store the data internally.
"""


import sublime
import sublime_plugin


class WindowSetProjectDataCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

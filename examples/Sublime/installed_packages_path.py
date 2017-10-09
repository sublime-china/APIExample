# coding:utf-8
"""
Class : sublime
Methods : installed_packages_path()
Return Value : str
Description : Returns the path where all the user's <span class="file">.sublime-package</span> files are located.
"""


import sublime
import sublime_plugin


class sublimeInstalledPackagesPathCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

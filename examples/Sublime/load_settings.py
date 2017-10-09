# coding:utf-8
"""
Class : sublime
Methods : load_settings(base_name)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.Settings">Settings</a>
Description : Loads the named settings. The name should include a file name and extension, but not a path. The packages will be searched for files matching the base_name, and the results will be collated into the settings object. Subsequent calls to load_settings() with the base_name will return the same object, and not load the settings from disk again.
"""


import sublime
import sublime_plugin


class sublimeLoadSettingsCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

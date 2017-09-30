# coding:utf-8
"""
Class : sublime
Methods : load_binary_resource(name)
Return Value : bytes
Description : Loads the given resource. The name should be in the format Packages/Default/Main.sublime-menu.
"""


import sublime
import sublime_plugin


class sublimeLoadBinaryResourceCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

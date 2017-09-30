# coding:utf-8
"""
Class : sublime
Methods : set_timeout(callback, delay)
Return Value : None
Description : Runs the callback in the main thread after the given delay (in milliseconds). Callbacks with an equal delay will be run in the order they were added.
"""


import sublime
import sublime_plugin


class sublimeSetTimeoutCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

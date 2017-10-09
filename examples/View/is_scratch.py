# coding:utf-8
"""
Class : sublime.View
Methods : is_scratch()
Return Value : bool
Description : Returns True if the buffer is a scratch buffer. Scratch buffers never report as being dirty.
"""


import sublime
import sublime_plugin


class ViewIsScratchCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

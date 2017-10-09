# coding:utf-8
"""
Class : sublime
Methods : get_clipboard(&lt;size_limit&gt;)
Return Value : str
Description : Returns the contents of the clipboard. size_limit is there to protect against unnecessarily large data, defaults to 16,777,216 characters
"""


import sublime
import sublime_plugin


class sublimeGetClipboardCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

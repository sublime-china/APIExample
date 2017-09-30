# coding:utf-8
"""
Class : sublime.Window
Methods : lookup_symbol_in_open_files(symbol)
Return Value : [<a href="http://www.sublimetext.com/docs/3/api_reference.html#type-location">location</a>]
Description : Returns all locations where the symbol is defined across open files.
"""


import sublime
import sublime_plugin


class WindowLookupSymbolInOpenFilesCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

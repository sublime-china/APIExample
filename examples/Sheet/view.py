# coding:utf-8
"""
Class : sublime.Sheet
Methods : view()
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a> <em>or</em> None
Description : Returns the view contained within the sheet. May be None if the sheet is an image preview, or the view has been closed.
"""


import sublime
import sublime_plugin


class SheetViewCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime.View
Methods : replace(edit, region, string)
Return Value : None
Description : Replaces the contents of the region with the given string.
"""


import sublime
import sublime_plugin


class ViewReplaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test replace region to "Happy everyday!"')
        region = self.view.sel()[0]
        self.replace(edit, region, "Happy everyday!")

    # 替换region区域的文本
    def replace(self, edit, region, string):
        self.view.replace(edit, region, string)

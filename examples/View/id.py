# coding:utf-8
"""
Class : sublime.View
Methods : id()
Return Value : int
Description : Returns a number that uniquely identifies this view.
"""


import sublime
import sublime_plugin


class ViewIdCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('current view id : ' + str(self.get_id()))

    # 获取当前View的id
    def get_id(self):
        return self.view.id()

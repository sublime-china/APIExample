# coding:utf-8
"""
Class : sublime.View
Methods : window()
Return Value : sublime.Window
Description : Returns a reference to the window containing the view.
"""


import sublime
import sublime_plugin


class ViewWindowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Get window : ' + str(self.get_window()))

    # 获取当前view所在的Window
    def get_window(self):
        return self.view.window()

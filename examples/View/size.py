# coding:utf-8
"""
Class : sublime.View
Methods : size()
Return Value : int
Description : Returns the number of character in the file.
"""


import sublime
import sublime_plugin


class ViewSizeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('The number of character in the file is ' + str(self.size()))

    # 获取文件里的字符总数
    def size(self):
        return self.view.size()

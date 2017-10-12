# coding:utf-8
"""
Class : sublime.View
Methods : name()
Return Value : str
Description : The name assigned to the buffer, if any
"""


import sublime
import sublime_plugin


class ViewNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Current buffer name : ' + self.get_name())

    # 获取当前buffer的名称，通常打开的文件名称未设置
    def get_name(self):
        return self.view.name()

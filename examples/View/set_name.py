# coding:utf-8
"""
Class : sublime.View
Methods : set_name(name)
Return Value : None
Description : Assigns a name to the buffer
"""


import sublime
import sublime_plugin


class ViewSetNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        name = self.view.name()
        print('Current buffer name is ' + name)
        print('Setting buffer name')
        self.set_name('Test Name')
        name = self.view.name()
        print('New buffer name is ' + name)

    # 设置buffer的名称
    def set_name(self, name):
        self.view.set_name(name)

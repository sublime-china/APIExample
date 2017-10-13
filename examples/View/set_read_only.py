# coding:utf-8
"""
Class : sublime.View
Methods : set_read_only(value)
Return Value : None
Description : Sets the read only property on the buffer.
"""


import sublime
import sublime_plugin


class ViewSetReadOnlyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Current file is read only : ' + str(self.view.is_read_only()))
        print('Setting file read only')
        self.set_read_only(True)
        print('Now file is read only')
        print('Try to type something, but not valid')

    # 设置当前文件只读
    def set_read_only(self, only):
        self.view.set_read_only(only)

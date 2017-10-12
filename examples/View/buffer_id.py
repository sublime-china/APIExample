# coding:utf-8
"""
Class : sublime.View
Methods : buffer_id()
Return Value : int
Description : Returns a number that uniquely identifies the buffer underlying this view.
"""


import sublime
import sublime_plugin


class ViewBufferIdCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('buffer id : ' + str(self.get_buffer_id()))

    # 获取当前View对应buffer的id
    def get_buffer_id(self):
        return self.view.buffer_id()

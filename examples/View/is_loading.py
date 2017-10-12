# coding:utf-8
"""
Class : sublime.View
Methods : is_loading()
Return Value : bool
Description : Returns True if the buffer is still loading from disk, and not ready for use.
"""


import sublime
import sublime_plugin


class ViewIsLoadingCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('buffer is still loading : ' + str(self.is_loading()))

    # 是否Buffer还在加载文件
    def is_loading(self):
        return self.view.is_loading()

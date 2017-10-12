# coding:utf-8
"""
Class : sublime.View
Methods : is_dirty()
Return Value : bool
Description : Returns True if there are any unsaved modifications to the buffer.
"""


import sublime
import sublime_plugin


class ViewIsDirtyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Current file is dirty and unsaved : ' + str(self.is_dirty()))

    # 是否有修改，未保存
    def is_dirty(self):
        return self.view.is_dirty()

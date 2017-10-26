# coding:utf-8
"""
Class : sublime.View
Methods : is_auto_complete_visible()
Return Value : bool
Description : Returns if the auto complete menu is currently visible.
"""


import sublime
import sublime_plugin


class ViewIsAutoCompleteVisibleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('is_auto_complete_visible : ' +
              str(self.is_auto_complete_visible()))

    # 自动完成的提示菜单是否显示
    # XXX : Test method with keyboard shortcuts
    def is_auto_complete_visible(self):
        return self.view.is_auto_complete_visible()

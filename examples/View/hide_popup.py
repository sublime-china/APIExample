# coding:utf-8
"""
Class : sublime.View
Methods : hide_popup()
Return Value : None
Description : Hides the popup.
"""


import sublime
import sublime_plugin


class ViewHidePopupCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('hide popup')
        self.hide_popup()

    # 隐藏 popup 悬浮框
    def hide_popup(self):
        self.view.hide_popup()

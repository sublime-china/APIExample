# coding:utf-8
"""
Class : sublime.View
Methods : is_popup_visible()
Return Value : bool
Description : Returns if the popup is currently shown.
"""


import sublime
import sublime_plugin


class ViewIsPopupVisibleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('is_popup_visible : ' + str(self.is_popup_visible()))

    # popup 悬浮框是否显示
    def is_popup_visible(self):
        return self.view.is_popup_visible()

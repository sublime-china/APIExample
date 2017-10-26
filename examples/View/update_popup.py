# coding:utf-8
"""
Class : sublime.View
Methods : update_popup(content)
Return Value : None
Description : Updates the contents of the currently visible popup.
"""


import sublime
import sublime_plugin


class ViewUpdatePopupCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test update popup content')
        print('Now show a popup first')
        show_content = '<p>Test upate popup</p>Now <a href="update">update</a>'
        self.view.show_popup(show_content, on_navigate=self.on_navigate)

    # 更新已经显示的弹出框内容
    def update_popup(self, content):
        self.view.update_popup(content)

    def on_navigate(self, string):
        if string == "update":
            if self.view.is_popup_visible():
                print('Update popup content')
                content = "Popup Content is updated!"
                self.update_popup(content)

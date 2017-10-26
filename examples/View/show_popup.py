# coding:utf-8
"""
Class : sublime.View
Methods : show_popup(content, <flags>, <location>, <max_width>, <max_height>, <on_navigate>, <on_hide>)
Return Value : None
Description : Shows a popup displaying HTML content.

    flags is a bitwise combination of the following:
        - sublime.COOPERATE_WITH_AUTO_COMPLETE. Causes the popup to display next to the auto complete menu
        - sublime.HIDE_ON_MOUSE_MOVE. Causes the popup to hide when the mouse is moved, clicked or scrolled
        - sublime.HIDE_ON_MOUSE_MOVE_AWAY. Causes the popup to hide when the mouse is moved (unless towards the popup), or when clicked or scrolled
    
    The default location of -1 will display the popup at the cursor, otherwise a text point should be passed.
    max_width and max_height set the maximum dimensions for the popup, after which scroll bars will be displayed.
    on_navigate is a callback that should accept a string contents of the href attribute on the link the user clicked.
    on_hide is called when the popup is hidden.


"""


import sublime
import sublime_plugin

import webbrowser


class ViewShowPopupCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test show popup')
        content = r'''<p>Test popup</p>
                    This is a <a href="navigate">navigate</a>
                    <p>click <a href="http://www.sublimetext.com/docs/3/api_reference.html">here</a> to open sublime API Reference</p>
                '''
        flags = sublime.HIDE_ON_MOUSE_MOVE_AWAY
        location = -1
        max_width = 400
        max_height = 300
        self.show_popup(content, flags, location, max_width,
                        max_height, self.on_navigate, self.on_hide)

    # 显示弹出框，内容为html格式的内容
    # 可设定最大宽度，最大高度，如果内容显示不够，会出现滚动条
    # on_navidate函数在点击链接时会触发（例如，点击 <a> 标签的内容)，函数参数为 href 属性的内容
    # on_hide函数在弹出框消失时触发
    def show_popup(self, content, flags=None, location=-1, max_width=None, max_height=None, on_navigate=None, on_hide=None):
        self.view.show_popup(content, flags, location,
                             max_width, max_height, on_navigate, on_hide)

    def on_navigate(self, string):
        print('href : ' + string)
        if string.startswith("http"):
            print('Open webrower')
            webbrowser.open_new_tab(string)

    def on_hide(self):
        print('popup is hidden')

# coding:utf-8
"""
Class sublime.View
Methods : sel()
Return Value : Selection
Description : Returns a reference to the selection.
"""
import sublime, sublime_plugin

class ViewSelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.show_selections()
        print(self.get_single_selection())
        print(self.get_multiple_selections())
        print(self.get_cursor_position())
        pass

    # 打印所有选区.
    def show_selections(self):
        print(x for x in self.view.sel())

    # 获取唯一的选区( sel()返回的List一定不为空, 失去焦点时, 选区为文件头, 即(0, 0) ).
    def get_single_selection(self):
        return self.view.sel()[0]

    # 获取所有选区.
    def get_multiple_selections(self):
        return self.view.sel()

    # 获取当前光标的位置.
    def get_cursor_position(self):
        region = self.view.sel()[0]
        return region.end()

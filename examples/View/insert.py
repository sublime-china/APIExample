# coding:utf-8
"""
Class : sublime.View
Methods : insert(edit, point, string)
Return Value : int
Description : Inserts the given string in the buffer at the specified point. Returns the number of characters inserted: this may be different if tabs are being translated into spaces in the current buffer.
"""


import sublime
import sublime_plugin


class ViewInsertCommand(sublime_plugin.TextCommand):

    head = r'''========================
	Hello Insert Head
========================

'''

    tail = r'''
========================
	Hello Insert Tail
========================
'''

    def run(self, edit):
        print('Test insert Head :  "Hello Insert Head" ')
        self.insert(edit, 0, self.head)
        print('Test insert tail :  "Hello Insert tail" ')
        self.insert(edit, self.view.size(), self.tail)

    # 插入文本
    def insert(self, edit, point, string):
        self.view.insert(edit, point, string)

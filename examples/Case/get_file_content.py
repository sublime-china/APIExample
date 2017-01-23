# coding:utf-8
"""
获取当前文件的内容
"""
import sublime, sublime_plugin

class GetFileContentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Returns the number of character in the file.
        # 文件内字符的长度
        fsize = self.view.size()

        # Creates a Region with initial values a and b.
        # 创建一个选区
        reg = sublime.Region(0, fsize)

        # Returns the contents of the region as a string.
        # 截取一个选区里的内容
        content = self.view.substr(reg)

        return content

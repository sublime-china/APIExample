# coding:utf-8
"""
Class : sublime.View
Methods : file_name()
Return Value : str
Description : The full name file the file associated with the buffer, or None if it doesn't exist on disk.
"""


import sublime
import sublime_plugin
import os


class ViewFileNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('File name : ' + self.get_file_name())
        print('File dir : ' + self.get_file_dir())
        print('Simple file name : ' + self.get_file_name())
        print('The ext with file ： ' + self.get_file_ext())

    # 获取文件名，包含全路径
    def get_file_name(self):
        fname = self.view.file_name()
        return fname

    # 获取文件所在文件夹路径
    def get_file_dir(self):
        fname = self.view.file_name()
        if fname:
            return os.path.dirname(fname)
        else:
            return None

    # 获取简单的文件名，不包含文件夹
    def get_simple_fname(self):
        fname = self.view.file_name()
        if fname:
            return os.path.basename(fname)
        else:
            return None

    # 获取文件名的后缀
    def get_file_ext(self):
        fname = self.view.file_name()
        if fname:
            name, ext = os.path.splitext(fname)
            return ext
        else:
            return None

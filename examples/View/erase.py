# coding:utf-8
"""
Class : sublime.View
Methods : erase(edit, region)
Return Value : None
Description : Erases the contents of the region from the buffer.
"""


import sublime
import sublime_plugin


class ViewEraseCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test erase content from first select region')
        region = self.view.sel()[0]
        if region.empty():
            print('You select nothing.')
            print('Now select a region and run test again')
            return
        region = self.view.sel()[0]
        self.erase(edit, region)
        print('Erase content : ' + self.view.substr(region))

    # 擦除region区域的文本
    def erase(self, edit, region):
        self.view.erase(edit, region)

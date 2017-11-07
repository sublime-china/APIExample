# coding:utf-8
"""
Class : sublime.View
Methods : full_line(point) | full_line(region)
Return Value : sublime.Region
Description : full_line(point) : As line(), but the region includes the trailing newline character, if any.
Description : full_line(region) : As line(), but the region includes the trailing newline character, if any.
"""


import sublime
import sublime_plugin


class ViewFullLineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test full_line(point)')
        point = self.view.sel()[0].b
        line_region = self.get_full_line_point(point)
        print('current select point in the line : ' +
              self.view.substr(line_region))
        print('Test full_line(region)')
        region = self.view.sel()[0]
        line_region = self.get_full_line_region(region)
        print('current select region in the line : ' +
              self.view.substr(line_region))

    # 获取point所在行的region区域
    def get_full_line_point(self, point):
        return self.view.full_line(point)

    # 获取region所在行的region区域，可以跨多行
    def get_full_line_region(self, region):
        return self.view.full_line(region)

# coding:utf-8
"""
Class : sublime.View
Methods : line(point) | line(region)
Return Value : sublime.Region
Description : line(point) : Returns the line that contains the point.
Description : line(region) : Returns a modified copy of region such that it starts at the beginning of a line, and ends at the end of a line. Note that it may span several lines.
"""


import sublime
import sublime_plugin


class ViewLineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test line(point)')
        point = self.view.sel()[0].b
        line_region = self.get_line_point(point)
        print('current select point in the line : ' +
              self.view.substr(line_region))
        print('Test line(region)')
        region = self.view.sel()[0]
        line_region = self.get_line_region(region)
        print('current select region in line : ' +
              self.view.substr(line_region))

    # 获取point所在行的region区域
    def get_line_point(self, point):
        return self.view.line(point)

    # 获取region所在行的region区域，可以跨多行
    def get_line_region(self, region):
        return self.view.line(region)

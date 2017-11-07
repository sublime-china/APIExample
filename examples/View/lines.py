# coding:utf-8
"""
Class : sublime.View
Methods : lines(region)
Return Value : sublime.Region
Description : Returns a list of lines (in sorted order) intersecting the region.
"""


import sublime
import sublime_plugin


class ViewLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test lines(region)')
        print('Select line : ')
        region = self.view.sel()[0]
        line_regions = self.get_lines(region)
        for line in line_regions:
            print('line : ' + self.view.substr(line))

        # 获取region区域包含的每一行整行region
    def get_lines(self, region):
        return self.view.lines(region)

# coding:utf-8
"""
Class : sublime.View
Methods : split_by_newlines(region)
Return Value : sublime.Region
Description : Splits the region up such that each region returned exists on exactly one line.
"""


import sublime
import sublime_plugin


class ViewSplitByNewlinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test split_by_newlines : ')
        region = self.view.sel()[0]
        line_regions = self.split_by_newlines(region)
        for line in line_regions:
            print('line : ' + self.view.substr(line))

    # 将region区域以行分隔成多个region
    # 与lines方法很像，lines方法强制为整行，这里不强制
    def split_by_newlines(self, region):
        return self.view.split_by_newlines(region)

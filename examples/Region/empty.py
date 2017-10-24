# coding:utf-8
"""
Class : sublime.Region
Methods : empty()
Return Value : bool
Description : Returns True iff begin() == end().
"""


import sublime
import sublime_plugin


# region.empty() 只单击鼠标，没有选中字符的时候，region为空，此时 a == b
class RegionEmptyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test region empty')
        print('Try to select a region from right to left and try to not select anything')
        region = self.view.sel()[0]
        print('region a is : ' + str(region.a))
        print('region b is : ' + str(region.b))
        print('region size is : ' + str(region.size()))
        print('region is empty : ' + str(region.empty()))

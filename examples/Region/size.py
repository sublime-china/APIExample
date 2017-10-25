# coding:utf-8
"""
Class : sublime.Region
Methods : size()
Return Value : int
Description : Returns the number of characters spanned by the region. Always >= 0.
"""


import sublime
import sublime_plugin


# region.size() 得到region范围包含的字符数，也是a,b的差值
class RegionSizeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test region size')
        print('Try to select a region from right to left')
        region = self.view.sel()[0]
        print('region a is : ' + str(region.a))
        print('region b is : ' + str(region.b))
        print('region size is : ' + str(region.size()))
        if region.empty():
        	print('region is empty. select a region and run test again.')

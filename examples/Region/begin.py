# coding:utf-8
"""
Class : sublime.Region
Methods : begin()
Return Value : int
Description : Returns the minimum of a and b.
"""


import sublime
import sublime_plugin


# region.begin() 得到region中a，b的较小值
class RegionBeginCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test region begin')
        print('Try to select a region from right to left')
        region = self.view.sel()[0]
        print('region a is : ' + str(region.a))
        print('region b is : ' + str(region.b))
        print('region begin is : ' + str(region.begin()))
        if region.empty():
        	print('region is empty. select a region and run test again.')

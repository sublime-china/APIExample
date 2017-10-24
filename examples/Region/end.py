# coding:utf-8
"""
Class : sublime.Region
Methods : end()
Return Value : int
Description : Returns the maximum of a and b.
"""


import sublime
import sublime_plugin


# region.end() 得到region中a，b的较大值
class RegionEndCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test region end')
        print('Try to select a region from right to left')
        region = self.view.sel()[0]
        print('region a is : ' + str(region.a))
        print('region b is : ' + str(region.b))
        print('region end is : ' + str(region.end()))
        if region.empty():
        	print('region is empty. select a region and run test again.')

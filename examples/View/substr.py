# coding:utf-8
"""
Class : sublime.View
Methods : substr(point) | substr(region)
Return Value : str
Description : substr(point): Returns the character to the right of the point.
Description : substr(region): Returns the contents of the region as a string.
"""


import sublime
import sublime_plugin


class ViewSubstrCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test substr(point)')
        r = self.view.sel()[0]
        p = r.b
        print('Select content from point')
        print(self.get_substr_point(p))

        print('Test substr(region)')
        r = self.view.sel()[0]
        if r.empty():
            print('You select nothing')
            print('Now select a region and run test again')
            return
        print('Select content from region : ')
        print(self.get_substr_region(r))

    # 获取Region区域的字符串
    def get_substr_region(self, region):
        return self.view.substr(region)

    # 获取Point点右边的字符
    def get_substr_point(self, point):
        return self.view.substr(point)

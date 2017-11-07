# coding:utf-8
"""
Class : sublime.View
Methods : word(point) | word(region)
Return Value : sublime.Region
Description : word(point) : Returns the word that contains the point.
Description : word(region) : Returns a modified copy of region such that it starts at the beginning of a word, and ends at the end of a word. Note that it may span several words.
"""


import sublime
import sublime_plugin


class ViewWordCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test word(point) : ')
        print('Select a point')
        point = self.view.sel()[0].b
        r = self.get_word_point(point)
        print('point in word : ' + self.view.substr(r))
        print('Test word(region) : ')
        print('Select a region')
        region = self.view.sel()[0]
        r = self.get_word_region(region)
        print('region in word : ' + self.view.substr(r))

    # 获取point所在的单词
    def get_word_point(self, point):
        return self.view.word(point)

    # 获取region所包含的单词
    def get_word_region(self, region):
        return self.view.word(region)

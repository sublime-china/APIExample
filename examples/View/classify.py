# coding:utf-8
"""
Class : sublime.View
Methods : classify(point)
Return Value : int
Description : <p>
                        Classifies point, returning a bitwise OR of zero or more of these flags:
                    </p>
                    <ul>
                        <li>sublime.CLASS_WORD_START</li>
                        <li>sublime.CLASS_WORD_END</li>
                        <li>sublime.CLASS_PUNCTUATION_START</li>
                        <li>sublime.CLASS_PUNCTUATION_END</li>
                        <li>sublime.CLASS_SUB_WORD_START</li>
                        <li>sublime.CLASS_SUB_WORD_END</li>
                        <li>sublime.CLASS_LINE_START</li>
                        <li>sublime.CLASS_LINE_END</li>
                        <li>sublime.CLASS_EMPTY_LINE</li>
                    </ul>
"""


import sublime
import sublime_plugin


class ViewClassifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

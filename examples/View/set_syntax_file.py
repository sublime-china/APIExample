# coding:utf-8
"""
Class : sublime.View
Methods : set_syntax_file(syntax_file)
Return Value : None
Description : Changes the syntax used by the view. syntax_file should be a name along the lines of Packages/Python/Python.tmLanguage. To retrieve the current syntax, use <code class=" language-python">view<span class="token punctuation">.</span>settings<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">'syntax'</span><span class="token punctuation">)</span></code>.
"""


import sublime
import sublime_plugin


class ViewSetSyntaxFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

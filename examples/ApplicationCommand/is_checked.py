# coding:utf-8
"""
Class : sublime_plugin.ApplicationCommand
Methods : is_checked(&lt;args&gt;)
Return Value : bool
Description : Returns True if a checkbox should be shown next to the menu item. The <span class="file">.sublime-menu</span> file must have the checkbox attribute set to true for this to be used.
"""


import sublime
import sublime_plugin


class ApplicationCommandIsCheckedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

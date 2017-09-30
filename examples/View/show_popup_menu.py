# coding:utf-8
"""
Class : sublime.View
Methods : show_popup_menu(items, on_done, &lt;flags&gt;)
Return Value : None
Description : <p>
                        Shows a pop up menu at the caret, to select an item in a list. on_done will be called once, with the index of the selected item. If the pop up menu was cancelled, on_done will be called with an argument of -1.
                    </p>

                    <p>
                        items is a list of strings.
                    </p>

                    <p>
                        flags it currently unused.
                    </p>
"""


import sublime
import sublime_plugin


class ViewShowPopupMenuCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

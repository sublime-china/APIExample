# coding:utf-8
"""
Class : sublime.Window
Methods : show_quick_panel(items, on_done, &lt;flags&gt;, &lt;selected_index&gt;, &lt;on_highlighted&gt;)
Return Value : None
Description : <p>
                        Shows a quick panel, to select an item in a list. on_done will be called once, with the index of the selected item. If the quick panel was cancelled, on_done will be called with an argument of -1.
                    </p>
                    <p>
                        items may be a list of strings, or a list of string lists. In the latter case, each entry in the quick panel will show multiple rows.
                    </p>
                    <p>
                        flags is a bitwise OR of sublime.MONOSPACE_FONT and sublime.KEEP_OPEN_ON_FOCUS_LOST
                    </p>
                    <p>
                        on_highlighted, if given, will be called every time the highlighted item in the quick panel is changed.
                    </p>
"""


import sublime
import sublime_plugin


class WindowShowQuickPanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

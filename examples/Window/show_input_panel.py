# coding:utf-8
"""
Class : sublime.Window
Methods : show_input_panel(caption, initial_text, on_done, on_change, on_cancel)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>
Description : Shows the input panel, to collect a line of input from the user. on_done and on_change, if not None, should both be functions that expect a single string argument. on_cancel should be a function that expects no arguments. The view used for the input widget is returned.
"""


import sublime
import sublime_plugin


class WindowShowInputPanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : applies_to_primary_view_only()
Return Value : bool
Description : A @classmethod that should return a bool indicating if this class applies only to the primary view for a file. A view is considered primary if it is the only, or first, view into a file.
"""


import sublime
import sublime_plugin


class ViewEventListenerAppliesToPrimaryViewOnlyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

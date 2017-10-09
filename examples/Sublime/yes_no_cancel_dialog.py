# coding:utf-8
"""
Class : sublime
Methods : yes_no_cancel_dialog(string, &lt;yes_title&gt;, &lt;no_title&gt;)
Return Value : int
Description : Displays a yes / no / cancel question dialog to the user. If yes_title and/or no_title are provided, they will be used as the text on the corresponding buttons on some platforms. Returns sublime.DIALOG_YES, sublime.DIALOG_NO or sublime.DIALOG_CANCEL.
"""


import sublime
import sublime_plugin


class sublimeYesNoCancelDialogCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

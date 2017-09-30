# coding:utf-8
"""
Class : sublime
Methods : ok_cancel_dialog(string, &lt;ok_title&gt;)
Return Value : bool
Description : Displays an ok / cancel question dialog to the user. If ok_title is provided, this may be used as the text on the ok button. Returns True if the user presses the ok button.
"""


import sublime
import sublime_plugin


class sublimeOkCancelDialogCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

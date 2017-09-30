# coding:utf-8
"""
Class : sublime.View
Methods : command_history(index, &lt;modifying_only&gt;)
Return Value : (str, dict, int)
Description : <p>
                        Returns the command name, command arguments, and repeat count for the given history entry, as stored in the undo / redo stack.
                    </p>

                    <p>
                        Index 0 corresponds to the most recent command, -1 the command before that, and so on. Positive values for index indicate to look in the redo stack for commands. If the undo / redo history doesn't extend far enough, then (None, None, 0) will be returned.
                    </p>

                    <p>
                        Setting modifying_only to True (the default is False) will only return entries that modified the buffer.
                    </p>
"""


import sublime
import sublime_plugin


class ViewCommandHistoryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

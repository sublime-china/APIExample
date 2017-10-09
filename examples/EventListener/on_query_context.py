# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_query_context(view, key, operator, operand, match_all)
Return Value : bool <em>or</em> None
Description : <p>
                        Called when determining to trigger a key binding with the given context key. If the plugin knows how to respond to the context, it should return either True of False. If the context is unknown, it should return None.
                    </p>

                    <p>
                        operator is one of:
                    </p>

                    <ul>
                        <li>
                            sublime.OP_EQUAL: Is the value of the context equal to the operand?
                        </li>
                        <li>
                            sublime.OP_NOT_EQUAL: Is the value of the context not equal to the operand?
                        </li>
                        <li>
                            sublime.OP_REGEX_MATCH: Does the value of the context match the regex given in operand?
                        </li>
                        <li>
                            sublime.OP_NOT_REGEX_MATCH: Does the value of the context not match the regex given in operand?
                        </li>
                        <li>
                            sublime.OP_REGEX_CONTAINS: Does the value of the context contain a substring matching the regex given in operand?
                        </li>
                        <li>
                            sublime.OP_NOT_REGEX_CONTAINS: Does the value of the context not contain a substring matching the regex given in operand?
                        </li>
                    </ul>

                    <p>
                        match_all should be used if the context relates to the selections: does every selection have to match (match_all == True), or is at least one matching enough (match_all == False)?
                    </p>
"""


import sublime
import sublime_plugin


class EventListenerOnQueryContextCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

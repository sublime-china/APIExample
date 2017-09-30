# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_hover(view, point, hover_zone)
Return Value : None
Description : <p>
                        Called when the user's mouse hovers over a view for a short period.
                    </p>

                    <p>
                        point is the closest point in the view to the mouse location. The mouse may not actually be located adjacent based on the value of hover_zone:
                    </p>

                    <ul>
                        <li>
                            sublime.HOVER_TEXT: When the mouse is hovered over text.
                        </li>
                        <li>
                            sublime.HOVER_GUTTER: When the mouse is hovered over the gutter.
                        </li>
                        <li>
                            sublime.HOVER_MARGIN: When the mouse is hovered in whitespace to the right of a line.
                        </li>
                    </ul>
"""


import sublime
import sublime_plugin


class EventListenerOnHoverCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

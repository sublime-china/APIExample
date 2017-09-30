# coding:utf-8
"""
Class : sublime.View
Methods : show_popup(content, &lt;flags&gt;, &lt;location&gt;, &lt;max_width&gt;, &lt;max_height&gt;, &lt;on_navigate&gt;, &lt;on_hide&gt;)
Return Value : None
Description : <p>
                        Shows a popup displaying HTML content.
                    </p>

                    <p>
                        flags is a bitwise combination of the following:
                    </p>

                    <ul>
                        <li>
                            sublime.COOPERATE_WITH_AUTO_COMPLETE. Causes the popup to display next to the auto complete menu
                        </li>
                        <li>
                            sublime.HIDE_ON_MOUSE_MOVE. Causes the popup to hide when the mouse is moved, clicked or scrolled
                        </li>
                        <li>
                            sublime.HIDE_ON_MOUSE_MOVE_AWAY. Causes the popup to hide when the mouse is moved (unless towards the popup), or when clicked or scrolled
                        </li>
                    </ul>

                    <p>
                        The default location of -1 will display the popup at the cursor, otherwise a text point should be passed.
                    </p>

                    <p>
                        max_width and max_height set the maximum dimensions for the popup, after which scroll bars will be displayed.
                    </p>

                    <p>
                        on_navigate is a callback that should accept a string contents of the href attribute on the link the user clicked.
                    </p>

                    <p>
                        on_hide is called when the popup is hidden.
                    </p>
"""


import sublime
import sublime_plugin


class ViewShowPopupCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

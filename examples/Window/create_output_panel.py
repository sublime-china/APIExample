# coding:utf-8
"""
Class : sublime.Window
Methods : create_output_panel(name, &lt;unlisted&gt;)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>
Description : <p>
                        Returns the view associated with the named output panel, creating it if required. The output panel can be shown by running the show_panel window command, with the panel argument set to the name with an "output." prefix.
                    </p>
                    <p>
                        The optional unlisted parameter is a boolean to control if the output panel should be listed in the panel switcher.
                    </p>
"""


import sublime
import sublime_plugin


class WindowCreateOutputPanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

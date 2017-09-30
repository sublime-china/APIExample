# coding:utf-8
"""
Class : sublime.Window
Methods : open_file(file_name, &lt;flags&gt;)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#sublime.View">View</a>
Description : <p>
                        Opens the named file, and returns the corresponding view. If the file is already opened, it will be brought to the front. Note that as file loading is asynchronous, operations on the returned view won't be possible until its is_loading() method returns False.
                    </p>
                    <p>
                        The optional flags parameter is a bitwise combination of:
                    </p>
                    <ul>
                        <li>
                            sublime.ENCODED_POSITION: Indicates the file_name should be searched for a :row or :row:col suffix
                        </li>
                        <li>
                            sublime.TRANSIENT: Open the file as a preview only: it won't have a tab assigned it until modified
                        </li>
                    </ul>
"""


import sublime
import sublime_plugin


class WindowOpenFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

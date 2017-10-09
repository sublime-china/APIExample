# coding:utf-8
"""
Class : sublime.Window
Methods : extract_variables()
Return Value : dict
Description : <p>
                        Returns a dictionary of strings populated with contextual keys:
                    </p>

                    <p>
                        packages, platform, file, file_path, file_name, file_base_name, file_extension, folder, project, project_path, project_name, project_base_name, project_extension. This dict is suitable for passing to sublime.expand_variables().
                    </p>
"""


import sublime
import sublime_plugin


class WindowExtractVariablesCommand(sublime_plugin.WindowCommand):

    def run(self):
        pass

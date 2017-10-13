# coding:utf-8
"""
Class : sublime.View
Methods : run_command(string, <args>)
Return Value : None
Description : Runs the named sublime.TextCommand with the (optional) given args.
"""


import sublime
import sublime_plugin


class ViewRunCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test run command : copy path')
        print('See the console log and status message')
        self.run_command("copy_path")

    # 运行TextCommand类型的命令
    def run_command(self, string, **args):
        self.view.run_command(string, args)

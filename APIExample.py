import sublime
import sublime_plugin
import os
import re

log_header = '[APIExample] '

example_path = os.path.join(os.path.dirname(__file__), 'examples')
fdir = os.path.dirname(__file__)


def get_files(path):
    if os.path.isfile(path):
        return [path]

    rlist = []
    for fname in os.listdir(path):
        unknownPath = os.path.join(path, fname)
        rlist.extend(get_files(unknownPath))

    return rlist


def get_file_path():
    filePaths = get_files(example_path)
    return filePaths


def split_path(filePaths):
    rlist = []
    for p in filePaths:
        path, fname = os.path.split(p)
        fname = fname.split('.')[0]
        rlist.append(fname)
    return rlist


def split_with_category(filePaths):
    rlist = []
    for file_path in filePaths:
        path, fname = os.path.split(file_path)
        fname = fname.split('.')[0]
        if '\\' in path:
            index = path.rfind('\\')
            path = path[index + 1:]
            rlist.append(path + " -> " + fname)
    return rlist


class ExampleShowInNewFileCommand(sublime_plugin.WindowCommand):
    # window.run_command('example_show_in_new_file', {'output':"helloworld"})

    def run_(self, edit_token, args):
        if args:
            output = args.get('output', 'content not set')
            fname = 'TestExample.py'
            filename = fdir + '/' + fname
            f = open(filename, 'w+')
            f.write(output)
            f.close()
            self.window.open_file(filename)


class ExampleShowListCommand(sublime_plugin.WindowCommand):
    def run(self):
        print(log_header + 'show example list')
        self.filePaths = get_file_path()
        showList = split_with_category(self.filePaths)
        self.window.show_quick_panel(showList, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        print(log_header + 'open file : ' + self.filePaths[index])
        f = open(self.filePaths[index], 'r', encoding='utf-8')
        content = f.read()
        f.close()
        self.window.run_command('example_show_in_new_file', {
            'output': content
        })


class ExampleRunTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get command and type then run command
        # type = window, view, application
        if self.view.file_name().endswith('TestExample.py'):
            region = sublime.Region(0, self.view.size())
            content = self.view.substr(region)
            restr = re.compile(
                r'class (.*?)Command\(.*?sublime_plugin\.(.*?)\):', re.S)
            items = re.findall(restr, content)
            for item in items:
                command = item[0]
                cmd_type = item[1]
                print(log_header + "command : " + command + ", type : " +
                      cmd_type)
                command = self.format_cmd(command)

                # show console panel before run command
                self.view.window().run_command('show_panel', {
                    "panel": "console",
                    "toggle": False
                })

                print(log_header + 'run command : ' + command)
                if cmd_type == "TextCommand":
                    self.view.run_command(command)
                elif cmd_type == "WindowCommand":
                    self.view.active_window().run_command(command)
                elif cmd_type == "ApplicationCommand":
                    sublime.run_command(command)
                else:
                    pass

    # eg: ApiRunTest -> api_run_test
    def format_cmd(self, cmd):
        rlist = []
        last_index = 0
        for i in range(len(cmd)):
            if cmd[i].isupper() and i != 0:
                rlist.append(cmd[last_index:i])
                last_index = i
        rlist.append(cmd[last_index:])
        return '_'.join(map(str.lower, rlist))


from .examples import *

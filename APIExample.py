
import sublime, sublime_plugin
import os

examplePath = os.path.join(os.path.dirname(__file__), 'examples')

def get_files(path):
    if os.path.isfile(path):
        return [path]

    rlist = []
    for fname in os.listdir(path):
        unknownPath = os.path.join(path, fname)
        rlist.extend(get_files(unknownPath))

    return rlist

def get_file_path():
    filePaths = get_files(examplePath)
    return filePaths

def split_path(filePaths):
    rlist = []
    for p in filePaths:
        path, fname = os.path.split(p)
        fname = fname.split('.')[0]
        rlist.append(fname)
    return rlist


class ShowExample(sublime_plugin.TextCommand):
    def run(self, edit, ExName=None):
        print(ExName)


class ShowExampleList(sublime_plugin.TextCommand):
    def run(self, edit):
        filePaths = get_file_path()
        print(split_path(filePaths))

        window = sublime.active_window()
        # window.show_quick_panel

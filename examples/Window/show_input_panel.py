# coding:utf-8
"""
Class sublime.Window
Methods : show_input_panel()
Return Value : View
Description : Shows the input panel, to collect a line of input from the user. on_done and on_change, if not None, should both be functions that expect a single string argument. on_cancel should be a function that expects no arguments. The view used for the input widget is returned.
"""
import sublime, sublime_plugin


class WindowShowInputPanelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # 回车确认之后的回调.
        def on_done(*argc, **argv):
            print()
            print("on_done :", argc)
            print("on_done :", argv)

        # 当"initial_text"发生改变时的回调.
        def on_change(*argc, **argv):
            print()
            print("on_change :", argc)
            print("on_change :", argv)

        # 按下ESC或者其他事件导致输入框取消时的回调.
        def on_cancel(*argc, **argv):
            print()
            print("on_cancel :", argc)
            print("on_cancel :", argv)

        window = sublime.active_window()
        window.show_input_panel("caption", "initial_text", on_done, on_change, on_cancel)

"""
1. 如果on_done, on_change, on_cancel, 只需要其中一部分回调时, 其他参数传None即可
2. 代码如上, 执行完window.show_input_panel(...)之后, 这个Class的run方法也就执行完毕了, 而在回调on_done的时候, edit是不存在的. 这样写只是为了好看:)
"""
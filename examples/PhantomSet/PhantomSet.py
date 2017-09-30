# coding:utf-8
"""
Class : sublime.PhantomSet
Methods : PhantomSet(view, &lt;key&gt;)
Return Value : None
Description : <p>
                        phantoms should be a list of phantoms.
                    </p>
                    <p>
                        The .region attribute of each existing phantom in the set will be updated.  New phantoms will be added to the view and phantoms not in phantoms list will be deleted.
                    </p>
"""


import sublime
import sublime_plugin


class PhantomSetPhantomsetCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

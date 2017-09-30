# coding:utf-8
"""
Class : sublime
Methods : expand_variables(value, variables)
Return Value : <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-value">value</a>
Description : Expands any variables in the string value using the variables defined in the dictionary variables. value may also be a list or dict, in which case the structure will be recursively expanded. Strings should use snippet syntax, for example: <code class=" language-python">expand_variables<span class="token punctuation">(</span><span class="token string">"Hello, ${name}"</span><span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token string">"name"</span><span class="token punctuation">:</span> <span class="token string">"Foo"</span><span class="token punctuation">}</span><span class="token punctuation">)</span></code>
"""


import sublime
import sublime_plugin


class sublimeExpandVariablesCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        pass

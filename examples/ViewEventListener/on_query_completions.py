# coding:utf-8
"""
Class : sublime_plugin.ViewEventListener
Methods : on_query_completions(prefix, locations)
Return Value : list<em>,</em> tuple <em>or</em> None
Description : <p>
                        Called whenever completions are to be presented to the user. The prefix is a unicode string of the text to complete.
                    </p>

                    <p>
                        locations is a list of <a href="http://www.sublimetext.com/docs/3/api_reference.html#type-point">points</a>. Since this method is called for all completions no matter the syntax, <code class=" language-python">self<span class="token punctuation">.</span>view<span class="token punctuation">.</span>match_selector<span class="token punctuation">(</span>point<span class="token punctuation">,</span> relevant_scope<span class="token punctuation">)</span></code> should be called to determine if the point is relevant.
                    </p>

                    <p>
                        The return value must be one of the following formats:
                    </p>

                    <ul>
                        <li>
                            <p>
                                None: no completions are provided
                            </p>
                            <p>
                                </p><pre class=" language-python"><code class=" language-python"><span class="token keyword">return</span> None</code></pre>
                            <p></p>
                        </li>
                        <li>
                            <p>
                                A list of 2-element lists/tuples. The first element is a unicode string of the completion trigger, the second is the unicode replacement text.
                            </p>
                            <p>
                                </p><pre class=" language-python"><code class=" language-python"><span class="token keyword">return</span> <span class="token punctuation">[</span><span class="token punctuation">[</span><span class="token string">"me1"</span><span class="token punctuation">,</span> <span class="token string">"method1()"</span><span class="token punctuation">]</span><span class="token punctuation">,</span> <span class="token punctuation">[</span><span class="token string">"me2"</span><span class="token punctuation">,</span> <span class="token string">"method2()"</span><span class="token punctuation">]</span><span class="token punctuation">]</span></code></pre>
                            <p></p>
                            <p>
                                The trigger may contain a tab character (\t) followed by a hint to display in the right-hand side of the completion box.
                            </p>
                            <p>
                                </p><pre class=" language-python"><code class=" language-python"><span class="token keyword">return</span> <span class="token punctuation">[</span>
    <span class="token punctuation">[</span><span class="token string">"me1\tmethod"</span><span class="token punctuation">,</span> <span class="token string">"method1()"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
    <span class="token punctuation">[</span><span class="token string">"me2\tmethod"</span><span class="token punctuation">,</span> <span class="token string">"method2()"</span><span class="token punctuation">]</span>
<span class="token punctuation">]</span></code></pre>
                            <p></p>
                            <p>
                                The replacement text may contain dollar-numeric fields such as a snippet does, e.g. $0, $1.
                            </p>
                            <p>
                                </p><pre class=" language-python"><code class=" language-python"><span class="token keyword">return</span> <span class="token punctuation">[</span>
    <span class="token punctuation">[</span><span class="token string">"fn"</span><span class="token punctuation">,</span> <span class="token string">"def ${1:name}($2) { $0 }"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
    <span class="token punctuation">[</span><span class="token string">"for"</span><span class="token punctuation">,</span> <span class="token string">"for ($1; $2; $3) { $0 }"</span><span class="token punctuation">]</span>
<span class="token punctuation">]</span></code></pre>
                            <p></p>
                        </li>
                        <li>
                            <p>
                                A 2-element tuple with the first element being the list format documented above, and the second element being bit flags from the following list:
                            </p>
                            <ul>
                                <li>
                                    sublime.INHIBIT_WORD_COMPLETIONS: prevent Sublime Text from showing completions based on the contents of the view
                                </li>
                                <li>
                                    sublime.INHIBIT_EXPLICIT_COMPLETIONS: prevent Sublime Text from showing completions based on .sublime-completions files
                                </li>
                            </ul>
                            <p>
                                </p><pre class=" language-python"><code class=" language-python"><span class="token keyword">return</span> <span class="token punctuation">(</span>
    <span class="token punctuation">[</span>
        <span class="token punctuation">[</span><span class="token string">"me1"</span><span class="token punctuation">,</span> <span class="token string">"method1()"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
        <span class="token punctuation">[</span><span class="token string">"me2"</span><span class="token punctuation">,</span> <span class="token string">"method2()"</span><span class="token punctuation">]</span>
    <span class="token punctuation">]</span><span class="token punctuation">,</span>
    sublime<span class="token punctuation">.</span>INHIBIT_WORD_COMPLETIONS <span class="token operator">|</span> sublime<span class="token punctuation">.</span>INHIBIT_EXPLICIT_COMPLETIONS
<span class="token punctuation">)</span></code></pre>
                            <p></p>
                        </li>
                    </ul>
"""


import sublime
import sublime_plugin


class ViewEventListenerOnQueryCompletionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

# coding:utf-8
"""
Class : sublime.View
Methods : add_regions(key, [regions], &lt;scope&gt;, &lt;icon&gt;, &lt;flags&gt;)
Return Value : None
Description : <p>
                        Add a set of regions to the view. If a set of regions already exists with the given key, they will be overwritten. The scope is used to source a color to draw the regions in, it should be the name of a scope, such as "comment" or "string". If the scope is empty, the regions won't be drawn.
                    </p>

                    <p>
                        The optional icon name, if given, will draw the named icons in the gutter next to each region. The icon will be tinted using the color associated with the scope. Valid icon names are dot, circle, bookmark and cross. The icon name may also be a full package relative path, such as Packages/Theme - Default/dot.png.
                    </p>

                    <p>
                        The optional flags parameter is a bitwise combination of:
                    </p>

                    <ul>
                        <li>
                            sublime.DRAW_EMPTY: Draw empty regions with a vertical bar. By default, they aren't drawn at all.
                        </li>
                        <li>
                            sublime.HIDE_ON_MINIMAP: Don't show the regions on the minimap.
                        </li>
                        <li>
                            sublime.DRAW_EMPTY_AS_OVERWRITE: Draw empty regions with a horizontal bar instead of a vertical one.
                        </li>
                        <li>
                            sublime.DRAW_NO_FILL: Disable filling the regions, leaving only the outline.
                        </li>
                        <li>
                            sublime.DRAW_NO_OUTLINE: Disable drawing the outline of the regions.
                        </li>
                        <li>
                            sublime.DRAW_SOLID_UNDERLINE: Draw a solid underline below the regions.
                        </li>
                        <li>
                            sublime.DRAW_STIPPLED_UNDERLINE: Draw a stippled underline below the regions.
                        </li>
                        <li>
                            sublime.DRAW_SQUIGGLY_UNDERLINE: Draw a squiggly underline below the regions.
                        </li>
                        <li>
                            sublime.PERSISTENT: Save the regions in the session.
                        </li>
                        <li>
                            sublime.HIDDEN: Don't draw the regions.
                        </li>
                    </ul>

                    <p>
                        The underline styles are exclusive, either zero or one of them should be given. If using an underline, sublime.DRAW_NO_FILL and sublime.DRAW_NO_OUTLINE should generally be passed in.
                    </p>
"""


import sublime
import sublime_plugin


class ViewAddRegionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass

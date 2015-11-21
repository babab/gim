gim
==============================================================================

gim is a simple command line tool for quickly creating Vim editing
sessions by choosing files from a selection menu gathered from the
output of the git ``status`` or ``ls-files`` subcommands.

When 2 files are selected it will fetch your terminal width and create a
vertical split window when > 161 characters are available. Otherwise the
files will be shown in a horizontal splitted window.

When >2 files are selected, all files will be opened as vim tabs.

usage
=====

::

   usage: gim [options]

   Edit files by picking them from git-status or git-ls-files output

   Options:
   -h, --help              show this help information
   -i, --indexed           Show indexed files only (git ls-files)
   -s, --staged            Do not include unstaged files
   -u, --unstaged          Include unstaged files [default]
   --vim=<vim executable>  Use an executable other then `vim`
   --version               show version information


install
=======

I have yet to write a setup.py script. Meanwhile you can just::

   $ sudo make install

Be sure to also install pycommand and optionally ansicolors.

dependencies
------------

- Python 3.5.x (lower versions may work but are not tested a.t.m)
- pycommand (needed) -- https://pypi.python.org/pypi/pycommand
- ansicolors (optional) -- https://pypi.python.org/pypi/ansicolors

uninstall
=========

I have yet to write a setup.py script. Meanwhile you can just::

   $ sudo make uninstall

license
=======

Copyright (c) 2013-2015 Benjamin Althues <benjamin@babab.nl>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
gim
==============================================================================

gim is a simple command line tool for quickly creating Vim or Emacs
editing sessions by choosing files from a selection menu gathered from
the output of the git ``status`` or ``ls-files`` subcommands.

Vim mode (default)
------------------

When 2 files are selected it will fetch your terminal width and create a
vertical split window when > 161 characters are available. Otherwise the
files will be shown in a horizontal splitted window.

When >2 files are selected, all files will be opened as vim tabs.

Emacs mode (-e or --emacs)
--------------------------

If -e or --emacs argument is given, each file will be opened in a new
Emacs frame with emacsclient.


.. image:: https://asciinema.org/a/e3hkjfe2pwna5timt14buxtwh.png
   :target: https://asciinema.org/a/e3hkjfe2pwna5timt14buxtwh
   :width: 640px


usage
=====

::

   usage: gim [options]

   Select files to be edited in Vim from Git repository data

   Options:
   -h, --help      show this help information
   -s, --staged    Do not include unstaged files
   -u, --unstaged  Include unstaged files [default]
   -i, --indexed   Show indexed files only (git ls-files)
   -1, --last      Show files of last commit
   -d, --diff      Open selected files with vimdiff
   -e, --emacs     Open selected files with Emacs
   --version       show version information


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

Copyright (c) 2013-2016 Benjamin Althues <benjamin@babab.nl>

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

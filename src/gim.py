'''Select files to be edited in Vim from Git repository data'''

# Copyright (c) 2013-2016 Benjamin Althues <benjamin@babab.nl>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os.path
import subprocess
import sys

import pycommand

try:
    from colors import green, red
except ImportError:
    green = red = lambda x: x

__version__ = '0.1.0'


class Gim:
    vim_executable = 'vim'

    def __init__(self, flags):
        self.flags = flags

    def statuslist(self):
        ls = subprocess.check_output(['git', 'status', '--short']) \
            .decode('UTF-8', errors='strict').split('\n')[:-1]

        ret = []
        n = 0
        for i in ls:
            if 'M' in i[:2] or 'A' in i[:2]:
                n += 1
                ret.append((n, green(i[0]), red(i[1]), i[3:]))
            elif 'UU' in i[:2]:
                n += 1
                ret.append((n, red(i[0]), red(i[1]), i[3:]))
            elif 'R' in i[:2]:
                n += 1
                ret.append((n, green('R'), red(i[1]), i[3:].split()[2]))
            elif '?' in i[:2] and not self.flags['staged']:
                n += 1
                ret.append((n, red(i[0]), red(i[1]), i[3:]))
        return ret

    def ls_files(self):
        ls = subprocess.check_output(['git', 'ls-files']) \
            .decode('UTF-8', errors='strict').split('\n')[:-1]
        ret = []
        n = 0
        for i in ls:
            n += 1
            ret.append((n, i))
        return ret

    def last_commit(self):
        files = subprocess.check_output(
            ['git', 'show', '--format=', '--name-only', '--no-show-signature']
        ).decode('UTF-8', errors='strict').split('\n')[:-1]
        ret = []
        n = 0
        for i in files:
            n += 1
            ret.append((n, i))
        return ret

    def vimargs(self, files):
        if self.flags.emacs:
            ret = ['emacsclient', '-q', '-n']
        elif self.flags.diff:
            ret = ['vimdiff']
        else:
            if len(files) == 1:
                ret = [self.vim_executable]
            elif len(files) == 2:
                cols = int(subprocess.check_output(['tput', 'cols'])
                           .decode('ascii', errors='strict'))
                if cols < 80:
                    ret = [self.vim_executable, '-p']
                elif cols < 191:
                    ret = [self.vim_executable, '-o']
                else:
                    ret = [self.vim_executable, '-O']
            else:
                ret = [self.vim_executable, '-p']

        args = ret + files
        print(green(' '.join(args)))
        return args


class ShellCommand(pycommand.CommandBase):
    '''Select files to be edited in Vim from Git repository data'''

    usagestr = 'usage: {0} [options]'.format(os.path.basename(sys.argv[0]))
    description = __doc__
    optionList = (
        ('help', ('h', False, 'show this help information')),
        ('staged', ('s', False, 'Do not include unstaged files')),
        ('unstaged', ('u', False, 'Include unstaged files [default]')),
        ('indexed', ('i', False, 'Show indexed files only (git ls-files)')),
        ('last', ('1', False, 'Show files of last commit')),
        ('diff', ('d', False, 'Open selected files with vimdiff')),
        ('emacs', ('e', False, 'Open selected files with Emacs')),
        ('version', ('', False, 'show version information')),
    )

    def run(self):
        if self.flags['help']:
            print(self.usage)
            return 0
        elif self.flags['version']:
            print('Gim version: {0} / Python version: {1} '
                  .format(__version__, sys.version.split()[0]))
            return 0

        self.gim = Gim(self.flags)

        print('Gim version {version}, run "gim --help" for more information'
              .format(version=__version__))

        if self.flags.indexed or self.flags.last:
            try:
                if self.flags.indexed:
                    gimFiles = self.gim.ls_files()
                elif self.flags.last:
                    gimFiles = self.gim.last_commit()
            except subprocess.CalledProcessError as e:
                return 2

            if not gimFiles:
                return 0

            padding = 2 if len(gimFiles) > 9 else 1
            for i in gimFiles:
                print('{0:{p}} {1}'
                      .format(i[0], i[1], p=padding))

            inp = input('\nSelect files to edit [{0}]: '
                        .format(green(gimFiles[0][1])))
            if not inp:
                inp = '1'

            files = []
            for i in inp.split():
                try:
                    files.append(gimFiles[int(i) - 1][1])
                except (IndexError, ValueError):
                    pass
        else:
            try:
                git_status = self.gim.statuslist()
            except subprocess.CalledProcessError as e:
                return 2

            if not git_status:
                return 0

            padding = 2 if len(git_status) > 9 else 1
            for i in git_status:
                print('{0:{p}} {1}{2} {3}'
                      .format(i[0], i[1], i[2], i[3], p=padding))

            inp = input('\nSelect files to edit [{0}]: '
                        .format(red(git_status[0][3])))
            inp = inp or '1'

            files = []
            for i in inp.split():
                try:
                    files.append(git_status[int(i) - 1][3])
                except (IndexError, ValueError):
                    pass

        if files:
            try:
                # Instead of `subprocess.call`, use `os.execvp` to
                # execute `Gim.vimargs()`, replacing the python process
                # of gim with the editor process.
                args = self.gim.vimargs(files)
                os.execvp(args[0], args)
            except IOError as e:
                print(e)
                return e.errno


def main(argv=sys.argv[1:]):
    """Main function for the CLI to be used as script (entry point)."""
    try:
        cmd = ShellCommand(argv)
        if cmd.error:
            print('error: {0}'.format(cmd.error))
            return 1
        else:
            return cmd.run()
    except (KeyboardInterrupt, EOFError):
        return 1


if __name__ == '__main__':
    sys.exit(main())

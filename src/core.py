import sys
import os
from subprocess import PIPE, Popen


class BaseModule(object):
    def __init__(self, manager):
        self.manager = manager

    def install(self):
        raise NotImplementedException('install method not implemented')


class Manager(object):
    def __init__(self, debug, verbose):
        self.debug = debug
        self.verbose = verbose

    def indentation(self, level=0):
        i = 4
        indent = ' ' * level * i
        max_length = 80 - (level * i)
        return indent, max_length

    def header(self, message, level=0):
        indent, max_length = self.indentation(level)
        print ''
        print indent + '-' * max_length
        print indent + message
        print indent + '-' * max_length

    def display(self, message=''):
        print message

    def info(self, message):
        print '    [INFO] ' + message

    def exec_cmd(self, cmd):
        if self.verbose:
            print '    $ ' + cmd + '\n'
        if not self.debug:
            os.system(cmd)

    def invoke(self, command):
        '''
        Invoke command as a new system process and return its output.
        '''
        return Popen(command, stdout=PIPE, shell=True).stdout.read()

    def info_confirm(self, question, level=1):
        indent, max_length = self.indentation(level)
        return self.confirm(question, prefix=indent + '[INFO] ')

    def confirm(self, question, default='no', prefix=''):
        valid = {'yes': True, 'y': True, 'ye': True, 'no': False, 'n': False}
        if default is None:
            prompt = ' [y/n] '
        elif default == 'yes':
            prompt = ' [Y/n] '
        elif default == 'no':
            prompt = ' [y/N] '
        else:
            raise ValueError('invalid default answer: [%s]' % default)

        while True:
            sys.stdout.write(prefix + question + prompt)
            choice = raw_input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write('Please respond with [yes] or [no] (or [y] or [n]).\n')

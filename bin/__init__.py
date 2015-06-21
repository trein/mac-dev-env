import sys
from subprocess import PIPE, Popen

MODE = 'DEBUG'
# MODE = 'VERBOSE'


def header(message, level=0):
    i = 4
    indent = ' ' * level * i
    dash = 80 - (level * i)
    print ''
    print indent + '-' * dash
    print indent + message
    print indent + '-' * dash


def display(message=''):
    print message


def info(message):
    print '    [INFO] ' + message


def exec_cmd(cmd):
    if MODE == 'DEBUG':
        return
    if MODE == 'VERBOSE':
        print cmd + '\n'
        return
    else:
        pass


def invoke(command):
    '''
    Invoke command as a new system process and return its output.
    '''
    return Popen(command, stdout=PIPE, shell=True).stdout.read()


def info_confirm(question):
    return confirm(question, prefix='    [INFO] ')


def confirm(question, default='no', prefix=''):
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

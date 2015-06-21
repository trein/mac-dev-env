from bin import *


def install():
    info('Installing pip...')
    exec_cmd('sudo easy_install pip')

    info('Installing virtualenv...')
    exec_cmd('sudo pip install virtualenv')

    info('Installing python3...')
    exec_cmd('brew install python3')

from bin import *


def install():
    if info_confirm('Do you want to install NodeJS stuff?'):
        info('Installing NodeJs...')
        exec_cmd('brew install node')

        info('Installing Grunt...')
        exec_cmd('npm install -g grunt-cli')

        info('Installing Composer...')
        exec_cmd('brew update')
        exec_cmd('brew install composer')

        info('Installing Bower...')
        exec_cmd('npm install -g bower')

        info('Installing Gulp...')
        exec_cmd('npm install --global gulp')

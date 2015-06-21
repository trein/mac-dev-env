from bin import *


def install():
    # xcode dev tools
    info('Installing xcode dev tools...')
    exec_cmd('xcode-select --install')

    # Oh my zsh installation
    info('Installing oh-my-zsh...')
    exec_cmd('curl -L http://install.ohmyz.sh | sh')

    # zsh fix
    fix_env = invoke('[[ -f /etc/zshenv ]]')
    if fix_env:
        info('Fixing OSX zsh environment bug ...')
        exec_cmd('sudo mv /etc/{zshenv,zshrc}')

    info('Installing git for control version')
    exec_cmd('brew install git')

    info('Installing irc client...')
    exec_cmd('brew install irssi')

    if info_confirm('Do you want to install GNU tools?'):
        info('Installing GNU core utilities...')
        exec_cmd('brew install coreutils')

        info('Installing GNU find, locate, updatedb and xargs...')
        exec_cmd('brew install findutils')

        info('Installing the most recent verions of some OSX tools')
        exec_cmd('brew tap homebrew/dupes')
        exec_cmd('brew install homebrew/dupes/grep')

        exec_cmd('printf \'export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"\' >> ~/.zshrc')
        exec_cmd('export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"')

    if info_confirm('Do you want to install Docker?'):
        info('Installing docker...')
        exec_cmd('brew install docker')
        exec_cmd('brew install boot2docker')

    # xquartz
    if info_confirm('Do you want to install xquartz?'):
        info('Installing xquartz...')
        exec_cmd('curl http://xquartz-dl.macosforge.org/SL/XQuartz-2.7.7.dmg -o /tmp/XQuartz.dmg')
        exec_cmd('open /tmp/XQuartz.dmg')

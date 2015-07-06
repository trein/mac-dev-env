from src.core import BaseModule


class Module(BaseModule):
    NAME = 'devtools_tools'

    def install(self):
        # xcode dev tools
        self.manager.info('Installing xcode dev tools...')
        self.manager.exec_cmd('xcode-select --install')

        # Oh my zsh installation
        self.manager.info('Installing oh-my-zsh...')
        self.manager.exec_cmd('curl -L http://install.ohmyz.sh | sh')

        # zsh fix
        fix_env = self.manager.invoke('[[ -f /etc/zshenv ]]')
        if fix_env:
            self.manager.info('Fixing OSX zsh environment bug ...')
            self.manager.exec_cmd('sudo mv /etc/{zshenv,zshrc}')

        self.manager.info('Installing git for control version')
        self.manager.exec_cmd('brew install git')

        self.manager.info('Installing irc client...')
        self.manager.exec_cmd('brew install irssi')

        if self.manager.info_confirm('Do you want to install GNU tools?'):
            self.manager.info('Installing GNU core utilities...')
            self.manager.exec_cmd('brew install coreutils')

            self.manager.info('Installing GNU find, locate, updatedb and xargs...')
            self.manager.exec_cmd('brew install findutils')

            self.manager.info('Installing the most recent verions of some OSX tools')
            self.manager.exec_cmd('brew tap homebrew/dupes')
            self.manager.exec_cmd('brew install homebrew/dupes/grep')

            self.manager.exec_cmd('printf \'export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"\' >> ~/.zshrc')
            self.manager.exec_cmd('export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"')

        if self.manager.info_confirm('Do you want to install Docker?'):
            self.manager.info('Installing docker...')
            self.manager.exec_cmd('brew install docker')
            self.manager.exec_cmd('brew install boot2docker')

        # xquartz
        if self.manager.info_confirm('Do you want to install xquartz?'):
            self.manager.info('Installing xquartz...')
            self.manager.exec_cmd('curl http://xquartz-dl.macosforge.org/SL/XQuartz-2.7.7.dmg -o /tmp/XQuartz.dmg')
            self.manager.exec_cmd('open /tmp/XQuartz.dmg')

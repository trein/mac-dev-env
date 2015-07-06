from src.core import BaseModule


class Module(BaseModule):
    NAME = 'osx_brew'

    def install(self):
        install_brew = self.manager.invoke('! command -v brew &>/dev/null')
        if install_brew:
            self.manager.info('Installing Homebrew, an OSX package manager, follow the instructions...')
            self.manager.exec_cmd('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

            adjust_path = self.manager.invoke('! grep -qs "recommended by brew doctor" ~/.zshrc')
            if adjust_path:
                self.manager.info('Put Homebrew location earlier in PATH ...')
                self.manager.exec_cmd('printf "\n# recommended by brew doctor\n" >> ~/.zshrc')
                self.manager.exec_cmd('printf "export PATH="/usr/local/bin:$PATH"\n" >> ~/.zshrc')
                self.manager.exec_cmd('export PATH="/usr/local/bin:$PATH"')
        else:
            self.manager.info('You already have Homebrew installed... Good job!')

        # Homebrew OSX libraries
        self.manager.info('Updating brew formulas')
        self.manager.exec_cmd('brew update')

        # Install brew cask
        self.manager.info('Installing cask to install apps')
        self.manager.exec_cmd('brew install caskroom/cask/brew-cask')
        self.manager.exec_cmd('brew tap caskroom/versions')

        # Install launchrocket
        self.manager.info('Installing launchrocket to manage your homebrew formulas like a champ!')
        self.manager.exec_cmd('brew cask install launchrocket')

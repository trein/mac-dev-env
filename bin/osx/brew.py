from bin import *


def install():
    install_brew = invoke('! command -v brew &>/dev/null')
    if install_brew:
        info('Installing Homebrew, an OSX package manager, follow the instructions...')
        exec_cmd('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

        adjust_path = invoke('! grep -qs "recommended by brew doctor" ~/.zshrc')
        if adjust_path:
            info('Put Homebrew location earlier in PATH ...')
            exec_cmd('printf "\n# recommended by brew doctor\n" >> ~/.zshrc')
            exec_cmd('printf "export PATH="/usr/local/bin:$PATH"\n" >> ~/.zshrc')
            exec_cmd('export PATH="/usr/local/bin:$PATH"')
    else:
        info('You already have Homebrew installed... Good job!')

    # Homebrew OSX libraries
    info('Updating brew formulas')
    exec_cmd('brew update')

    # Install brew cask
    info('Installing cask to install apps')
    exec_cmd('brew install caskroom/cask/brew-cask')
    exec_cmd('brew tap caskroom/versions')

    # Install launchrocket
    info('Installing launchrocket to manage your homebrew formulas like a champ!')
    exec_cmd('brew cask install launchrocket')

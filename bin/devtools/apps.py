from bin import *


def install():
    apps = [
        'java',
        'vagrant',
        'iterm2',
        'eclipse-jee',
        'rubymine',
        'pycharm',
        'hex-fiend',
        'android-studio',
        'little-snitch',
        'qlcolorcode',
        'qlstephen',
        'qlmarkdown',
        'quicklook-json',
        'qlprettypatch',
        'quicklook-csv',
        'betterzipql',
        'webpquicklook',
        'suspicious-package',
        'virtualbox',
        'anvil',
        'brackets',
        'carbon-copy-cloner',
        'cyberduck',
        'tomighty',
    ]

    # Install apps to /Applications
    # Default is: /Users/$user/Applications
    for app in apps:
        exec_cmd('brew cask install --appdir="/Applications" %s' % app)

    ###############################################################################
    # Sublime Text
    ###############################################################################
    info('Setting up package manager for Sublime Text')
    exec_cmd('cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/')
    exec_cmd('git clone git://github.com/wbond/sublime_package_control.git Package\ Control')
    exec_cmd('cd -1')

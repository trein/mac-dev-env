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

    ###############################################################################
    # iTerm2
    ###############################################################################
    info('Setting up iTerm2')
    exec_cmd('defaults write com.googlecode.iterm2 ShowPaneTitles -int 0')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :"Keyboard Map":"Use Bold Font" false" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf702-0x320000" dict" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf702-0x320000":Action integer 18" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf702-0x320000":Text string \"\"" ~/Library/Preferences/com.googlecode.iterm2.plist')

    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf703-0x320000" dict" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf703-0x320000":Action integer 19" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf703-0x320000":Text string \"\"" ~/Library/Preferences/com.googlecode.iterm2.plist')

    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf700-0x320000" dict" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf700-0x320000":Action integer 20" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf700-0x320000":Text string \"\"" ~/Library/Preferences/com.googlecode.iterm2.plist')

    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf701-0x320000" dict" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf701-0x320000":Action integer 21" ~/Library/Preferences/com.googlecode.iterm2.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Add :GlobalKeyMap:"0xf701-0x320000":Text string \"\"" ~/Library/Preferences/com.googlecode.iterm2.plist')

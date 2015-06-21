from bin import *


def install():
    apps = [
        'arq',
        'dropbox',
        'appcleaner',
        'google-chrome',
        'firefox',
        'spotify',
        'flash',
        'sublime-text3',
        'sketch',
        'vlc',
        'lightpaper',
        'skype',
        'transmission',
    ]

    # Install apps to /Applications
    # Default is: /Users/$user/Applications
    for app in apps:
        exec_cmd('brew cask install --appdir="/Applications" %s' % app)

    ###############################################################################
    # Transmission.app
    ###############################################################################
    if info_confirm('Do you use Transmission for torrenting?'):
        info('Use `~/Downloads/Incomplete` to store incomplete downloads')
        exec_cmd('defaults write org.m0k.transmission UseIncompleteDownloadFolder -bool true')
        exec_cmd('mkdir -p ~/Downloads/Incomplete')
        exec_cmd('defaults write org.m0k.transmission IncompleteDownloadFolder -string "${HOME}/Downloads/Incomplete"')

        info('Don\'t prompt for confirmation before downloading')
        exec_cmd('defaults write org.m0k.transmission DownloadAsk -bool false')

        info('Trash original torrent files')
        exec_cmd('defaults write org.m0k.transmission DeleteOriginalTorrent -bool true')

        info('Hide the donate message')
        exec_cmd('defaults write org.m0k.transmission WarningDonate -bool false')

        info('Hide the legal disclaimer')
        exec_cmd('defaults write org.m0k.transmission WarningLegal -bool false')

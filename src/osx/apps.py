from src.core import BaseModule


class Module(BaseModule):
    NAME = 'osx_apps'

    def install(self):
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
            self.manager.exec_cmd('brew cask install --appdir="/Applications" %s' % app)

        ###############################################################################
        # Transmission.app
        ###############################################################################
        if self.manager.info_confirm('Do you use Transmission for torrenting?'):
            self.manager.info('Use `~/Downloads/Incomplete` to store incomplete downloads')
            self.manager.exec_cmd('defaults write org.m0k.transmission UseIncompleteDownloadFolder -bool true')
            self.manager.exec_cmd('mkdir -p ~/Downloads/Incomplete')
            self.manager.exec_cmd('defaults write org.m0k.transmission IncompleteDownloadFolder -string "${HOME}/Downloads/Incomplete"')

            self.manager.info('Don\'t prompt for confirmation before downloading')
            self.manager.exec_cmd('defaults write org.m0k.transmission DownloadAsk -bool false')

            self.manager.info('Trash original torrent files')
            self.manager.exec_cmd('defaults write org.m0k.transmission DeleteOriginalTorrent -bool true')

            self.manager.info('Hide the donate message')
            self.manager.exec_cmd('defaults write org.m0k.transmission WarningDonate -bool false')

            self.manager.info('Hide the legal disclaimer')
            self.manager.exec_cmd('defaults write org.m0k.transmission WarningLegal -bool false')

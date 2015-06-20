#!/bin/sh
###############################################################################
# OSX applications
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

apps=(
  arq
  dropbox
  appcleaner
  google-chrome
  firefox
  spotify
  flash
  sublime-text3
  sketch
  vlc
  lightpaper
  skype
  transmission
)

# Install apps to /Applications
# Default is: /Users/$user/Applications
pretty_print "installing apps..."
brew cask install --appdir="/Applications" ${apps[@]}

###############################################################################
# Transmission.app                                                            #
###############################################################################pretty_print
pretty_print "Do you use Transmission for torrenting? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Use `~/Downloads/Incomplete` to store incomplete downloads"
    defaults write org.m0k.transmission UseIncompleteDownloadFolder -bool true
    mkdir -p ~/Downloads/Incomplete
    defaults write org.m0k.transmission IncompleteDownloadFolder -string "${HOME}/Downloads/Incomplete"

    pretty_print "Don't prompt for confirmation before downloading"
    defaults write org.m0k.transmission DownloadAsk -bool false

    pretty_print "Trash original torrent files"
    defaults write org.m0k.transmission DeleteOriginalTorrent -bool true

    pretty_print "Hide the donate message"
    defaults write org.m0k.transmission WarningDonate -bool false

    pretty_print "Hide the legal disclaimer"
    defaults write org.m0k.transmission WarningLegal -bool false
    break;;
  *) break;;
esac
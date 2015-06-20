#!/bin/sh
###############################################################################
# OSX applications
###############################################################################

extra_apps=(
  screenflick
  appzapper
  slack
  asepsis
  shiori
  flux
  atom
  postbox
  tower
  cloudup
  droplr
  github
  openoffice
  parallels-desktop
  smcfancontrol
  fluid
  harvest
  miro
  keka
  unrarx
  sequel-pro
)

dev_apps=(
  vagrant
  iterm2
  qlcolorcode
  qlstephen
  qlmarkdown
  quicklook-json
  qlprettypatch
  quicklook-csv
  betterzipql
  webpquicklook
  suspicious-package
  virtualbox
  anvil
  brackets
  carbon-copy-cloner
  cyberduck
  tomighty
)

# Install apps to /Applications
# Default is: /Users/$user/Applications
pretty_print "installing dev apps..."
brew cask install --appdir="/Applications" ${dev_apps[@]}

###############################################################################
# Sublime Text
###############################################################################
pretty_print "Setting up package manager for Sublime Text"
  cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
  git clone git://github.com/wbond/sublime_package_control.git Package\ Control
  cd -1

pretty_print "Do you use Sublime Text 3 as your editor of choice, and is it installed?"
read -r response
case $response in
  [yY])
    # Installing from homebrew cask does the following for you!
    # echo ""
    # echo "Linking Sublime Text for command line usage as subl"
    # ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

    # pretty_print "Setting Git to use Sublime Text as default editor"
    # git config --global core.editor "subl -n -w"
    break;;
  *) break;;
esac

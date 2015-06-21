#!/bin/sh
###############################################################################
# Development tools
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

# xcode dev tools
pretty_print "Installing xcode dev tools..."
  xcode-select --install

# Oh my zsh installation
pretty_print "Installing oh-my-zsh..."
  curl -L http://install.ohmyz.sh | sh

# zsh fix
if [[ -f /etc/zshenv ]]; then
  pretty_print "Fixing OSX zsh environment bug ..."
    sudo mv /etc/{zshenv,zshrc}
fi

pretty_print "Installing git for control version"
  brew install git

pretty_print "Installing irc client..."
  brew install irssi

pretty_print "Do you want to install GNU tools? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing GNU core utilities..."
      brew install coreutils

    pretty_print "Installing GNU find, locate, updatedb and xargs..."
      brew install findutils

    pretty_print "Installing the most recent verions of some OSX tools"
      brew tap homebrew/dupes
      brew install homebrew/dupes/grep

    printf 'export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"' >> ~/.zshrc
    export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"
    break;;
  *) break;;
esac

pretty_print "Do you want to install Docker? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing docker..."
      brew install docker
      brew install boot2docker
    break;;
  *) break;;
esac

# xquartz
pretty_print "Do you want to install xquartz? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing xquartz..."
      curl http://xquartz-dl.macosforge.org/SL/XQuartz-2.7.7.dmg -o /tmp/XQuartz.dmg
      open /tmp/XQuartz.dmg
    break;;
  *) break;;
esac
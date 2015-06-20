#!/bin/sh
###############################################################################
# Homebrew installation
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

if ! command -v brew &>/dev/null; then
  pretty_print "Installing Homebrew, an OSX package manager, follow the instructions..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

  if ! grep -qs "recommended by brew doctor" ~/.zshrc; then
    pretty_print "Put Homebrew location earlier in PATH ..."
      printf '\n# recommended by brew doctor\n' >> ~/.zshrc
      printf 'export PATH="/usr/local/bin:$PATH"\n' >> ~/.zshrc
      export PATH="/usr/local/bin:$PATH"
  fi
else
  pretty_print "You already have Homebrew installed... Good job!"
fi

# Homebrew OSX libraries
pretty_print "Updating brew formulas"
  brew update

# Install brew cask
pretty_print "Installing cask to install apps"
  brew install caskroom/cask/brew-cask
  brew tap caskroom/versions

pretty_print "Installing launchrocket to manage your homebrew formulas like a champ!"
  brew cask install launchrocket
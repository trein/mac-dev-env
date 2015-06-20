#!/bin/sh

# Some things taken from here
# https://github.com/mathiasbynens/dotfiles/blob/master/.osx

pretty_print() {
  printf "\n%b\n" "$1"
}

pretty_print "setting up your dev environment like a boss..."

# Set continue to false by default
CONTINUE=false

echo ""
pretty_print "###############################################"
pretty_print "#        DO NOT RUN THIS SCRIPT BLINDLY       #"
pretty_print "#         YOU'LL PROBABLY REGRET IT...        #"
pretty_print "#                                             #"
pretty_print "#              READ IT THOROUGHLY             #"
pretty_print "#         AND EDIT TO SUIT YOUR NEEDS         #"
pretty_print "###############################################"
echo ""

echo ""
pretty_print "Have you read through the script you're about to run and "
pretty_print "understood that it will make changes to your computer? (y/n)"
read -r response
case $response in
  [yY]) CONTINUE=true
      break;;
  *) break;;
esac

if ! $CONTINUE; then
  # Check if we're continuing and output a message if not
  pretty_print "Please go read the script, it only takes a few minutes"
  exit
fi

# Here we go.. ask for the administrator password upfront and run a
# keep-alive to update existing `sudo` time stamp until script has finished
sudo -v
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

###############################################################################
# OSX customizations
###############################################################################
pretty_print "------------------------------"
pretty_print "Initializing OSX customizations..."
  sh general/osx.sh

###############################################################################
# Homebrew installation
###############################################################################
pretty_print "------------------------------"
pretty_print "Installing homebrew..."
  sh general/brew.sh

###############################################################################
# OSX useful fonts
###############################################################################
pretty_print "------------------------------"
pretty_print "Installing fonts..."
  sh general/fonts.sh

###############################################################################
# OSX applications
###############################################################################
pretty_print "------------------------------"
pretty_print "Installing apps..."
  sh general/apps.sh

# when done with cask
brew update && brew upgrade brew-cask && brew cleanup && brew cask cleanup

###############################################################################
# Development tools
###############################################################################
pretty_print "------------------------------"
pretty_print "Installing development tools..."
echo ""
echo "Do you want to install development tools?"
read -r response
case $response in
  [yY])
    sh dev/tools.sh
    sh dev/apps.sh
    sh dev/vim.sh
    sh dev/dbs.sh
    sh dev/node.sh
    sh dev/ruby.sh
    sh dev/python.sh
    break;;
  *) break;;
esac

###############################################################################
# Restoring apps settings
###############################################################################
pretty_print "------------------------------"
pretty_print "Restoring settings files..."
# Install Mackup
pretty_print "Installing Mackup..."
  brew install mackup

# Launch it and restoring your files
pretty_print "Running Mackup Restore..."
  mackup restore

###############################################################################
# Kill affected applications
###############################################################################
echo ""
pretty_print "Shits Done Bro! You still need to manually install package installer "
pretty_print "within sublime, setup your hosts, httpd.conf and vhosts files, "
pretty_print "download chrome extensions, setup your hotspots/mouse settings, "
pretty_print "and setup your git shit - look at readme for more info."
echo ""
echo ""
pretty_print "################################################################################"
echo ""
echo ""
pretty_print "Note that some of these changes require a logout/restart to take effect."
pretty_print "Killing some open applications in order to take effect."
echo ""

find ~/Library/Application\ Support/Dock -name "*.db" -maxdepth 1 -delete
for app in "Activity Monitor" "Address Book" "Calendar" "Contacts" "cfprefsd" \
  "Dock" "Finder" "Mail" "Messages" "Safari" "SystemUIServer" \
  "Terminal" "Transmission"; do
  killall "${app}" > /dev/null 2>&1
done
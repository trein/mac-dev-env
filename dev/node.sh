#!/bin/sh
###############################################################################
# Node tools
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

pretty_print "Do you want to install NodeJS stuff? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing NodeJs..."
      brew install node

    pretty_print "Installing Grunt..."
      npm install -g grunt-cli

    pretty_print "Installing Composer..."
      brew update
      brew install composer

    pretty_print "Installing Bower..."
      npm install -g bower

    pretty_print "Installing Gulp..."
      npm install --global gulp
    break;;
  *) break;;
esac
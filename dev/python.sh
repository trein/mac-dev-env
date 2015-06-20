#!/bin/sh
###############################################################################
# Python tools
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

pretty_print "Installing pip..."
  easy_install pip

pretty_print "Installing python3..."
  brew install python3

pretty_print "Installing virtualenv..."
  pip install virtualenv
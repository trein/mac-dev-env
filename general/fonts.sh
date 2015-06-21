#!/bin/sh
###############################################################################
# Installing fonts
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

fonts=(
  font-m-plus
  font-clear-sans
  font-roboto
  font-open-sans
  font-source-sans-pro
  font-alegreya
  font-montserrat
  font-inconsolata
  font-pt-sans
  font-quattrocento-sans
  font-quicksand
  font-raleway
  font-sorts-mill-goudy
  font-ubuntu
)

# install fonts
pretty_print "Do you want to install additional fonts? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing some caskroom/fonts..."
    brew tap caskroom/fonts

    pretty_print "Installing the fonts..."
    brew cask install ${fonts[@]}
    break;;
  *) break;;
esac

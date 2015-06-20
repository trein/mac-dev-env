#!/bin/sh
###############################################################################
# Development databases
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

pretty_print "Do you want to install MySQL? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing mysql..."
      brew install mysql
      brew unlink mysql
    break;;
  *) break;;
esac

pretty_print "Do you want to install Postgres? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing postgres..."
      brew install postgres
    break;;
  *) break;;
esac

pretty_print "Do you want to install MariaDB? (y/n)"
read -r response
case $response in
  [yY])
    pretty_print "Installing mariadb..."
      brew install mariadb # Install MariaDB
      # mysql setup auto start and start the database
      ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents
      launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
      # Run the Database Installer
      unset TMPDIR
      cd /usr/local/Cellar/mariadb/{VERSION}
      mysql_install_db
      mysql.server start # Start MariaDB
      mysql_secure_installation # Secure the Installation
    break;;
  *) break;;
esac
from bin import *


def install():
    if info_confirm('Do you want to install MySQL?'):
        info('Installing mysql...')
        exec_cmd('brew install mysql')
        exec_cmd('brew unlink mysql')

    if info_confirm('Do you want to install Postgres?'):
        info('Installing postgres...')
        exec_cmd('brew install postgres')

    if info_confirm('Do you want to install MariaDB?'):
        info('Installing mariadb...')
        exec_cmd('brew install mariadb # Install MariaDB')
        # mysql setup auto start and start the database
        exec_cmd('ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents')
        exec_cmd('launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist')
        # Run the Database Installer
        exec_cmd('unset TMPDIR')
        exec_cmd('cd /usr/local/Cellar/mariadb/{VERSION}')
        exec_cmd('mysql_install_db')
        exec_cmd('mysql.server start # Start MariaDB')
        exec_cmd('mysql_secure_installation # Secure the Installation')

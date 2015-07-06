from src.core import BaseModule


class Module(BaseModule):
    NAME = 'devtools_dbs'

    def install(self):
        if self.manager.info_confirm('Do you want to install MySQL?'):
            self.manager.info('Installing mysql...')
            self.manager.exec_cmd('brew install mysql')
            self.manager.exec_cmd('brew unlink mysql')

        if self.manager.info_confirm('Do you want to install Postgres?'):
            self.manager.info('Installing postgres...')
            self.manager.exec_cmd('brew install postgres')

        if self.manager.info_confirm('Do you want to install MariaDB?'):
            self.manager.info('Installing mariadb...')
            self.manager.exec_cmd('brew install mariadb # Install MariaDB')
            # mysql setup auto start and start the database
            self.manager.exec_cmd('ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents')
            self.manager.exec_cmd('launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist')
            # Run the Database Installer
            self.manager.exec_cmd('unset TMPDIR')
            self.manager.exec_cmd('cd /usr/local/Cellar/mariadb/{VERSION}')
            self.manager.exec_cmd('mysql_install_db')
            self.manager.exec_cmd('mysql.server start # Start MariaDB')
            self.manager.exec_cmd('mysql_secure_installation # Secure the Installation')

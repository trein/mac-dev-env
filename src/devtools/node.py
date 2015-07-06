from src.core import BaseModule


class Module(BaseModule):
    NAME = 'devtools_node'

    def install(self):
        if self.manager.info_confirm('Do you want to install NodeJS stuff?'):
            self.manager.info('Installing NodeJs...')
            self.manager.exec_cmd('brew install node')

            self.manager.info('Installing Grunt...')
            self.manager.exec_cmd('npm install -g grunt-cli')

            self.manager.info('Installing Composer...')
            self.manager.exec_cmd('brew update')
            self.manager.exec_cmd('brew install composer')

            self.manager.info('Installing Bower...')
            self.manager.exec_cmd('npm install -g bower')

            self.manager.info('Installing Gulp...')
            self.manager.exec_cmd('npm install --global gulp')

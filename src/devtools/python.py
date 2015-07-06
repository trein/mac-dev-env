from src.core import BaseModule


class Module(BaseModule):
    NAME = 'devtools_python'

    def install(self):
        self.manager.info('Installing pip...')
        self.manager.exec_cmd('sudo easy_install pip')

        self.manager.info('Installing virtualenv...')
        self.manager.exec_cmd('sudo pip install virtualenv')

        self.manager.info('Installing python3...')
        self.manager.exec_cmd('brew install python3')

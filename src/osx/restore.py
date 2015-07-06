from src.core import BaseModule


class Module(BaseModule):
    NAME = 'osx_restore'

    def install(self):
    	self.manager.header('Restoring settings files...')
        if self.manager.confirm('Do you want to restore apps settings?'):
            self.manager.display()
            # Install Mackup
            self.manager.info('Installing Mackup...')
            self.manager.exec_cmd('brew install mackup')
            # Launch it and restoring your files
            self.manager.info('Running Mackup Restore...')
            self.manager.exec_cmd('mackup restore')
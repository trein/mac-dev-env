from src.core import BaseModule


class Module(BaseModule):
    NAME = 'osx_fonts'

    def install(self):
        fonts = [
            'font-m-plus',
            'font-clear-sans',
            'font-roboto',
            'font-open-sans',
            'font-source-sans-pro',
            'font-alegreya',
            'font-montserrat',
            'font-inconsolata',
            'font-pt-sans',
            'font-quattrocento-sans',
            'font-quicksand',
            'font-raleway',
            'font-sorts-mill-goudy',
            'font-ubuntu',
        ]

        # install fonts
        if self.manager.info_confirm('Do you want to install additional fonts?'):
            self.manager.info('Installing some caskroom/fonts...')
            self.manager.exec_cmd('brew tap caskroom/fonts')
            for f in fonts:
                self.manager.exec_cmd('brew cask install %s' % f)

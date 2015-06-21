from bin import *


def install():
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
    if info_confirm('Do you want to install additional fonts?'):
        info('Installing some caskroom/fonts...')
        exec_cmd('brew tap caskroom/fonts')
        for f in fonts:
            exec_cmd('brew cask install %s' % f)

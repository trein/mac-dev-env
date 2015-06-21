from bin import *
import prefs
import fonts
import brew
import apps


def setup():
    # OSX preferences
    header('Setting up OSX preferences...', 1)
    prefs.setup()
    display()

    # OSX useful fonts
    header('Installing fonts...', 1)
    fonts.install()
    display()

    # Homebrew installation
    header('Installing homebrew...', 1)
    brew.install()
    display()

    # OSX applications
    header('Installing apps...', 1)
    apps.install()
    display()

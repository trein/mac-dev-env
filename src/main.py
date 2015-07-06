import collections
import src.core

import osx.prefs
import osx.brew
import osx.fonts
import osx.apps
import osx.restore

import devtools.apps
import devtools.dbs
import devtools.node
import devtools.python
import devtools.ruby
import devtools.tools
import devtools.vim


MODULES = collections.OrderedDict((
    (osx.prefs.Module.NAME, osx.prefs.Module),
    (osx.brew.Module.NAME, osx.brew.Module),
    (osx.fonts.Module.NAME, osx.fonts.Module),
    (osx.apps.Module.NAME, osx.apps.Module),

    (devtools.tools.Module.NAME, devtools.tools.Module),
    (devtools.apps.Module.NAME, devtools.apps.Module),
    (devtools.dbs.Module.NAME, devtools.dbs.Module),
    (devtools.node.Module.NAME, devtools.node.Module),
    (devtools.python.Module.NAME, devtools.python.Module),
    (devtools.ruby.Module.NAME, devtools.ruby.Module),
    (devtools.vim.Module.NAME, devtools.vim.Module),

    (osx.restore.Module.NAME, osx.restore.Module),
))


class Installer(object):
    def __init__(self, args):
        self.modules = args.modules
        self.manager = src.core.Manager(args.debug, args.verbose)

    def start(self):
        self.manager.display('Setting up your dev environment like a boss...')
        self.show_disclaimer()

        # Here we go.. ask for the administrator password upfront and run a
        # keep-alive to update existing `sudo` time stamp until script has finished
        self.manager.exec_cmd('sudo -v')
        self.manager.exec_cmd('while true; do sudo -n true; sleep 60; kill -0 \'$$\' || exit; done 2>/dev/null &')

        self.manager.header('Installing modules')
        for module_name, module_class in MODULES.items():
            if not self.modules or module_name in self.modules:
                # only installs declared modules
                self.manager.header('Initializing module [%s]...' % module_name, 1)
                if self.manager.info_confirm('Do you want to setup [%s]?' % module_name):
                    self.manager.display()
                    module_class(self.manager).install()

        self.cleanup()


    def show_disclaimer(self):
        self.manager.display('')
        self.manager.display('###############################################')
        self.manager.display('#        DO NOT RUN THIS SCRIPT BLINDLY       #')
        self.manager.display('#         YOU WILL PROBABLY REGRET IT...      #')
        self.manager.display('#                                             #')
        self.manager.display('#              READ IT THOROUGHLY             #')
        self.manager.display('#         AND EDIT TO SUIT YOUR NEEDS         #')
        self.manager.display('###############################################')
        self.manager.display('')

        message = ('Have you read through the script you are about to run and '
                   'understood that it will make changes to your computer?')

        if not self.manager.confirm(message):
          # Check if we're continuing and output a message if not
            self.manager.display('Please go read the script, it only takes a few minutes')
            exit()

    def cleanup(self):
        self.manager.header('Cleaning up setup...')
        self.manager.info('Cleaning up Brew Cask...')
        self.manager.exec_cmd('brew update && brew upgrade brew-cask && brew cleanup && brew cask cleanup')

        self.manager.display('\n')
        self.manager.display('Shits Done Bro! You still need to manually install package installer ')
        self.manager.display('within sublime, setup your hosts, httpd.conf and vhosts files, ')
        self.manager.display('download chrome extensions, setup your hotspots/mouse settings, ')
        self.manager.display('and setup your git shit - look at readme for more info.')
        self.manager.display('\n')
        self.manager.display('Note that some of these changes require a logout/restart to take effect.')
        self.manager.display('Killing some open applications in order to take effect.')
        self.manager.display('')

        apps = [
            'Activity Monitor',
            'Address Book',
            'Calendar',
            'Contacts',
            'cfprefsd',
            'Dock',
            'Finder',
            'Mail',
            'Messages',
            'Safari',
            'SystemUIServer',
            'Terminal',
        ]

        self.manager.exec_cmd('find ~/Library/Application\ Support/Dock -name \'*.db\' -maxdepth 1 -delete')
        for app in apps:
            self.manager.exec_cmd('killall %s > /dev/null 2>&1' % app)

from bin import *

display('Setting up your dev environment like a boss...')

# Set continue to false by default
CONTINUE = False

display('')
display('###############################################')
display('#        DO NOT RUN THIS SCRIPT BLINDLY       #')
display('#         YOU WILL PROBABLY REGRET IT...      #')
display('#                                             #')
display('#              READ IT THOROUGHLY             #')
display('#         AND EDIT TO SUIT YOUR NEEDS         #')
display('###############################################')
display('')

message = ('Have you read through the script you are about to run and '
           'understood that it will make changes to your computer?')
if not confirm(message):
  # Check if we're continuing and output a message if not
    display('Please go read the script, it only takes a few minutes')
    exit()

# Here we go.. ask for the administrator password upfront and run a
# keep-alive to update existing `sudo` time stamp until script has finished
exec_cmd('sudo -v')
exec_cmd('while true; do sudo -n true; sleep 60; kill -0 \'$$\' || exit; done 2>/dev/null &')

###############################################################################
# OSX setup
###############################################################################
header('Initializing OSX setup...')
if confirm('Do you want to setup OSX?'):
    display()
    import bin.osx as osx
    osx.setup()

###############################################################################
# Development tools
###############################################################################
header('Installing development tools...')
if confirm('Do you want to install development tools?'):
    display()
    import bin.devtools as devtools
    devtools.install()

###############################################################################
# Restoring apps settings
###############################################################################
header('Restoring settings files...')
if confirm('Do you want to restore apps settings?'):
    display()
    # Install Mackup
    info('Installing Mackup...')
    exec_cmd('brew install mackup')
    # Launch it and restoring your files
    info('Running Mackup Restore...')
    exec_cmd('mackup restore')

###############################################################################
# Cleaning up setup
###############################################################################
header('Cleaning up setup...')
info('Cleaning up Brew Cask...')
exec_cmd('brew update && brew upgrade brew-cask && brew cleanup && brew cask cleanup')

display('\n')
display('Shits Done Bro! You still need to manually install package installer ')
display('within sublime, setup your hosts, httpd.conf and vhosts files, ')
display('download chrome extensions, setup your hotspots/mouse settings, ')
display('and setup your git shit - look at readme for more info.')
display('\n')
display('Note that some of these changes require a logout/restart to take effect.')
display('Killing some open applications in order to take effect.')
display('')

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

exec_cmd('find ~/Library/Application\ Support/Dock -name \'*.db\' -maxdepth 1 -delete')
for app in apps:
    exec_cmd('killall %s > /dev/null 2>&1' % app)

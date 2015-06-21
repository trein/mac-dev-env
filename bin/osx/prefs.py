from bin import *


def set_optional():
    ###############################################################################
    # System settings
    ###############################################################################
    if info_confirm('Would you like to set your computer name (as done via System Preferences >> Sharing)?'):
        computer_name = raw_input('    >>> What would you like it to be? ')
        exec_cmd('sudo scutil --set ComputerName %s' % computer_name)
        exec_cmd('sudo scutil --set HostName %s' % computer_name)
        exec_cmd('sudo scutil --set LocalHostName %s' % computer_name)
        exec_cmd('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string %s' % computer_name)

    ###############################################################################
    # Finder
    ###############################################################################
    if info_confirm('Show hidden files in Finder by default?'):
        exec_cmd('defaults write com.apple.Finder AppleShowAllFiles -bool true')

    if info_confirm('Show dotfiles in Finder by default?'):
        exec_cmd('defaults write com.apple.finder AppleShowAllFiles TRUE')

    if info_confirm('Show all filename extensions in Finder by default?'):
        exec_cmd('defaults write NSGlobalDomain AppleShowAllExtensions -bool true')

    if info_confirm('Use column view in all Finder windows by default?'):
        exec_cmd('defaults write com.apple.finder FXPreferredViewStyle Clmv')

    if info_confirm('Avoid creation of .DS_Store files on network volumes?'):
        exec_cmd('defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true')

    ###############################################################################
    # Time Machine
    ###############################################################################
    if info_confirm('Prevent Time Machine from prompting to use new hard drives as backup volume?'):
        exec_cmd('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')


def set_defaults():
    ###############################################################################
    # System settings
    ###############################################################################
    info('Check for software updates daily, not just once per week')
    exec_cmd('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')

    info('Always show scrollbars')
    # Possible values: `WhenScrolling`, `Automatic` and `Always`
    exec_cmd('defaults write NSGlobalDomain AppleShowScrollBars -string "Always"')

    info('Expand save panel by default')
    exec_cmd('defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true')
    exec_cmd('defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true')

    info('Expand print panel by default')
    exec_cmd('defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true')
    exec_cmd('defaults write NSGlobalDomain PMPrintingExpandedStateForPrint2 -bool true')

    info('Save to disk (not to iCloud) by default')
    exec_cmd('defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false')

    info('Automatically quit printer app once the print jobs complete')
    exec_cmd('defaults write com.apple.print.PrintingPrefs "Quit When Finished" -bool true')

    ################################################################################
    # Trackpad, mouse, keyboard, Bluetooth accessories, and input
    ################################################################################
    info('Increasing sound quality for Bluetooth headphones/headsets')
    exec_cmd('defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Min (editable)" -int 40')

    info('Disable "natural" (Lion-style) scrolling')
    exec_cmd('defaults write NSGlobalDomain com.apple.swipescrolldirection -bool false')

    # Set a blazingly fast keyboard repeat rate
    info('Set a blazingly fast keyboard repeat rate')
    exec_cmd('defaults write NSGlobalDomain KeyRepeat -int 1')

    info('Tap to click')
    exec_cmd('defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad Clicking -bool true')

    info('Tap with two fingers to emulate right click')
    exec_cmd('defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad TrackpadRightClick -bool true')

    # Set a shorter Delay until key repeat
    info('Set a shorter Delay until key repeat')
    exec_cmd('defaults write NSGlobalDomain InitialKeyRepeat -int 12')

    info('Use all keyboard function keys (F1, F2, etc) as standard keys')
    exec_cmd('defaults write NSGlobalDomain "com.apple.keyboard.fnState" "1"')

    ###############################################################################
    # Finder
    ###############################################################################
    info('Show icons for hard drives, servers, and removable media on the desktop')
    exec_cmd('defaults write com.apple.finder ShowExternalHardDrivesOnDesktop -bool true')
    exec_cmd('defaults write com.apple.finder ShowHardDrivesOnDesktop -bool true')
    exec_cmd('defaults write com.apple.finder ShowMountedServersOnDesktop -bool true')
    exec_cmd('defaults write com.apple.finder ShowRemovableMediaOnDesktop -bool true')

    info('Show item info near icons on the desktop and in other icon views')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:showItemInfo true" ~/Library/Preferences/com.apple.finder.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :StandardViewSettings:IconViewSettings:showItemInfo true" ~/Library/Preferences/com.apple.finder.plist')

    info('Increase grid spacing for icons on the desktop and in other icon views')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:gridSpacing 100" ~/Library/Preferences/com.apple.finder.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :StandardViewSettings:IconViewSettings:gridSpacing 100" ~/Library/Preferences/com.apple.finder.plist')

    info('Allowing text selection in Quick Look/Preview in Finder by default')
    exec_cmd('defaults write com.apple.finder QLEnableTextSelection -bool true')

    info('Enabling snap-to-grid for icons on the desktop and in other icon views')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:arrangeBy grid" ~/Library/Preferences/com.apple.finder.plist')
    exec_cmd('/usr/libexec/PlistBuddy -c "Set :StandardViewSettings:IconViewSettings:arrangeBy grid" ~/Library/Preferences/com.apple.finder.plist')

    info('Enabling the Develop menu and the Web Inspector in Safari')
    exec_cmd('defaults write com.apple.Safari IncludeDevelopMenu -bool true')
    exec_cmd('defaults write com.apple.Safari WebKitDeveloperExtrasEnabledPreferenceKey -bool true')
    exec_cmd('defaults write com.apple.Safari "com.apple.Safari.ContentPageGroupIdentifier.WebKit2DeveloperExtrasEnabled" -bool true')

    info('Adding a context menu item for showing the Web Inspector in web views')
    exec_cmd('defaults write NSGlobalDomain WebKitDeveloperExtras -bool true')

    # Use current directory as default search scope in Finder
    info('Use current directory as default search scope in Finder')
    exec_cmd('defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"')

    # Show Path bar in Finder
    info('Show Path bar in Finder')
    exec_cmd('defaults write com.apple.finder ShowPathbar -bool true')

    # Show Status bar in Finder
    info('Show Status bar in Finder')
    exec_cmd('defaults write com.apple.finder ShowStatusBar -bool true')

    # Show indicator lights for open applications in the Dock
    info('Show indicator lights for open applications in the Dock')
    exec_cmd('defaults write com.apple.dock show-process-indicators -bool true')

    # Show the ~/Library folder
    info('Show the ~/Library folder')
    exec_cmd('chflags nohidden ~/Library')

    ###############################################################################
    # Dock, Dashboard, and hot corners
    ###############################################################################
    info('Enable highlight hover effect for the grid view of a stack (Dock)')
    exec_cmd('defaults write com.apple.dock mouse-over-hilite-stack -bool true')

    info('Set the icon size of Dock items to 36 pixels')
    exec_cmd('defaults write com.apple.dock tilesize -int 36')

    info('Show indicator lights for open applications in the Dock')
    exec_cmd('defaults write com.apple.dock show-process-indicators -bool true')

    info('Speed up Mission Control animations')
    exec_cmd('defaults write com.apple.dock expose-animation-duration -float 0.1')

    info('Don\'t group windows by application in Mission Control')
    # (i.e. use the old Expose behavior instead)
    exec_cmd('defaults write com.apple.dock expose-group-by-app -bool false')

    info('Don\'t automatically rearrange Spaces based on most recent use')
    exec_cmd('defaults write com.apple.dock mru-spaces -bool false')

    info('Dock hiding setup')
    # Automatically hide and show the Dock
    exec_cmd('defaults write com.apple.dock autohide -bool true')
    exec_cmd('defaults write com.apple.dock mru-spaces -bool false')
    # Remove the auto-hiding Dock delay
    exec_cmd('defaults write com.apple.dock autohide-delay -float 0')
    # Remove the animation when hiding/showing the Dock
    exec_cmd('defaults write com.apple.dock autohide-time-modifier -float 0')

    # Hot corners
    # Possible values:
    #  0: no-op
    #  2: Mission Control
    #  3: Show application windows
    #  4: Desktop
    #  5: Start screen saver
    #  6: Disable screen saver
    #  7: Dashboard
    # 10: Put display to sleep
    # 11: Launchpad
    # 12: Notification Center
    # Top left screen corner -> Desktop
    exec_cmd('defaults write com.apple.dock wvous-tl-corner -int 4')
    exec_cmd('defaults write com.apple.dock wvous-tl-modifier -int 0')
    # Top right screen corner -> Mission Control
    exec_cmd('defaults write com.apple.dock wvous-tr-corner -int 2')
    exec_cmd('defaults write com.apple.dock wvous-tr-modifier -int 0')
    # Bottom right screen corner -> Start screen saver
    exec_cmd('defaults write com.apple.dock wvous-br-corner -int 5')
    exec_cmd('defaults write com.apple.dock wvous-br-modifier -int 0')

    ###############################################################################
    # Mail
    ###############################################################################
    info('Setting email addresses to copy as "foo@example.com" instead of "Foo Bar <foo@example.com>" in Mail.app')
    exec_cmd('defaults write com.apple.mail AddressesIncludeNameOnPasteboard -bool false')

    info('Display emails in threaded mode, sorted by date (oldest at the top)')
    exec_cmd('defaults write com.apple.mail DraftsViewerAttributes -dict-add "DisplayInThreadedMode" -string "yes"')
    exec_cmd('defaults write com.apple.mail DraftsViewerAttributes -dict-add "SortedDescending" -string "yes"')
    exec_cmd('defaults write com.apple.mail DraftsViewerAttributes -dict-add "SortOrder" -string "received-date"')

    ###############################################################################
    # Terminal
    ###############################################################################
    info('Enabling UTF-8 ONLY in Terminal.app and setting the Pro theme by default')
    exec_cmd('defaults write com.apple.terminal StringEncodings -array 4')
    exec_cmd('defaults write com.apple.Terminal "Default Window Settings" -string "Pro"')
    exec_cmd('defaults write com.apple.Terminal "Startup Window Settings" -string "Pro"')


def setup():
    set_optional()
    set_defaults()

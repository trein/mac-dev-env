from src.core import BaseModule


class Module(BaseModule):
    NAME = 'osx_prefs'

    def install(self):
        self.set_optional()
        self.set_defaults()

    def set_optional(self):
        ###############################################################################
        # System settings
        ###############################################################################
        if self.manager.info_confirm('Would you like to set your computer name (as done via System Preferences >> Sharing)?'):
            computer_name = raw_input('    >>> What would you like it to be? ')
            self.manager.exec_cmd('sudo scutil --set ComputerName %s' % computer_name)
            self.manager.exec_cmd('sudo scutil --set HostName %s' % computer_name)
            self.manager.exec_cmd('sudo scutil --set LocalHostName %s' % computer_name)
            self.manager.exec_cmd('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string %s' % computer_name)

        ###############################################################################
        # Finder
        ###############################################################################
        if self.manager.info_confirm('Show hidden files in Finder by default?'):
            self.manager.exec_cmd('defaults write com.apple.Finder AppleShowAllFiles -bool true')

        if self.manager.info_confirm('Show dotfiles in Finder by default?'):
            self.manager.exec_cmd('defaults write com.apple.finder AppleShowAllFiles TRUE')

        if self.manager.info_confirm('Show all filename extensions in Finder by default?'):
            self.manager.exec_cmd('defaults write NSGlobalDomain AppleShowAllExtensions -bool true')

        if self.manager.info_confirm('Use column view in all Finder windows by default?'):
            self.manager.exec_cmd('defaults write com.apple.finder FXPreferredViewStyle Clmv')

        if self.manager.info_confirm('Avoid creation of .DS_Store files on network volumes?'):
            self.manager.exec_cmd('defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true')

        ###############################################################################
        # Time Machine
        ###############################################################################
        if self.manager.info_confirm('Prevent Time Machine from prompting to use new hard drives as backup volume?'):
            self.manager.exec_cmd('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')


    def set_defaults(self):
        ###############################################################################
        # System settings
        ###############################################################################
        self.manager.info('Check for software updates daily, not just once per week')
        self.manager.exec_cmd('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')

        self.manager.info('Always show scrollbars')
        # Possible values: `WhenScrolling`, `Automatic` and `Always`
        self.manager.exec_cmd('defaults write NSGlobalDomain AppleShowScrollBars -string "Always"')

        self.manager.info('Expand save panel by default')
        self.manager.exec_cmd('defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true')
        self.manager.exec_cmd('defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true')

        self.manager.info('Expand print panel by default')
        self.manager.exec_cmd('defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true')
        self.manager.exec_cmd('defaults write NSGlobalDomain PMPrintingExpandedStateForPrint2 -bool true')

        self.manager.info('Save to disk (not to iCloud) by default')
        self.manager.exec_cmd('defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false')

        self.manager.info('Automatically quit printer app once the print jobs complete')
        self.manager.exec_cmd('defaults write com.apple.print.PrintingPrefs "Quit When Finished" -bool true')

        ################################################################################
        # Trackpad, mouse, keyboard, Bluetooth accessories, and input
        ################################################################################
        self.manager.info('Increasing sound quality for Bluetooth headphones/headsets')
        self.manager.exec_cmd('defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Min (editable)" -int 40')

        self.manager.info('Disable "natural" (Lion-style) scrolling')
        self.manager.exec_cmd('defaults write NSGlobalDomain com.apple.swipescrolldirection -bool false')

        # Set a blazingly fast keyboard repeat rate
        self.manager.info('Set a blazingly fast keyboard repeat rate')
        self.manager.exec_cmd('defaults write NSGlobalDomain KeyRepeat -int 1')

        self.manager.info('Tap to click')
        self.manager.exec_cmd('defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad Clicking -bool true')

        self.manager.info('Tap with two fingers to emulate right click')
        self.manager.exec_cmd('defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad TrackpadRightClick -bool true')

        # Set a shorter Delay until key repeat
        self.manager.info('Set a shorter Delay until key repeat')
        self.manager.exec_cmd('defaults write NSGlobalDomain InitialKeyRepeat -int 12')

        self.manager.info('Use all keyboard function keys (F1, F2, etc) as standard keys')
        self.manager.exec_cmd('defaults write NSGlobalDomain "com.apple.keyboard.fnState" "1"')

        ###############################################################################
        # Finder
        ###############################################################################
        self.manager.info('Show icons for hard drives, servers, and removable media on the desktop')
        self.manager.exec_cmd('defaults write com.apple.finder ShowExternalHardDrivesOnDesktop -bool true')
        self.manager.exec_cmd('defaults write com.apple.finder ShowHardDrivesOnDesktop -bool true')
        self.manager.exec_cmd('defaults write com.apple.finder ShowMountedServersOnDesktop -bool true')
        self.manager.exec_cmd('defaults write com.apple.finder ShowRemovableMediaOnDesktop -bool true')

        self.manager.info('Disable Mission Control and Application Windows keyboard shortcuts')
        self.manager.exec_cmd('defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 33 "{ enabled = 1; value = { parameters = (65535, 125, 262144); type = \'standard\'; }; }"')
        self.manager.exec_cmd('defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 34 "{ enabled = 1; value = { parameters = (65535, 126, 393216); type = \'standard\'; }; }"')

        self.manager.info('Show item info near icons on the desktop and in other icon views')
        self.manager.exec_cmd('/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:showItemInfo true" ~/Library/Preferences/com.apple.finder.plist')
        self.manager.exec_cmd('/usr/libexec/PlistBuddy -c "Set :StandardViewSettings:IconViewSettings:showItemInfo true" ~/Library/Preferences/com.apple.finder.plist')

        self.manager.info('Increase grid spacing for icons on the desktop and in other icon views')
        self.manager.exec_cmd('/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:gridSpacing 100" ~/Library/Preferences/com.apple.finder.plist')
        self.manager.exec_cmd('/usr/libexec/PlistBuddy -c "Set :StandardViewSettings:IconViewSettings:gridSpacing 100" ~/Library/Preferences/com.apple.finder.plist')

        self.manager.info('Allowing text selection in Quick Look/Preview in Finder by default')
        self.manager.exec_cmd('defaults write com.apple.finder QLEnableTextSelection -bool true')

        self.manager.info('Enabling snap-to-grid for icons on the desktop and in other icon views')
        self.manager.exec_cmd('/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:arrangeBy grid" ~/Library/Preferences/com.apple.finder.plist')
        self.manager.exec_cmd('/usr/libexec/PlistBuddy -c "Set :StandardViewSettings:IconViewSettings:arrangeBy grid" ~/Library/Preferences/com.apple.finder.plist')

        self.manager.info('Enabling the Develop menu and the Web Inspector in Safari')
        self.manager.exec_cmd('defaults write com.apple.Safari IncludeDevelopMenu -bool true')
        self.manager.exec_cmd('defaults write com.apple.Safari WebKitDeveloperExtrasEnabledPreferenceKey -bool true')
        self.manager.exec_cmd('defaults write com.apple.Safari "com.apple.Safari.ContentPageGroupIdentifier.WebKit2DeveloperExtrasEnabled" -bool true')

        self.manager.info('Adding a context menu item for showing the Web Inspector in web views')
        self.manager.exec_cmd('defaults write NSGlobalDomain WebKitDeveloperExtras -bool true')

        # Use current directory as default search scope in Finder
        self.manager.info('Use current directory as default search scope in Finder')
        self.manager.exec_cmd('defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"')

        # Show Path bar in Finder
        self.manager.info('Show Path bar in Finder')
        self.manager.exec_cmd('defaults write com.apple.finder ShowPathbar -bool true')

        # Show Status bar in Finder
        self.manager.info('Show Status bar in Finder')
        self.manager.exec_cmd('defaults write com.apple.finder ShowStatusBar -bool true')

        # Show indicator lights for open applications in the Dock
        self.manager.info('Show indicator lights for open applications in the Dock')
        self.manager.exec_cmd('defaults write com.apple.dock show-process-indicators -bool true')

        # Show the ~/Library folder
        self.manager.info('Show the ~/Library folder')
        self.manager.exec_cmd('chflags nohidden ~/Library')

        ###############################################################################
        # Dock, Dashboard, and hot corners
        ###############################################################################
        self.manager.info('Enable highlight hover effect for the grid view of a stack (Dock)')
        self.manager.exec_cmd('defaults write com.apple.dock mouse-over-hilite-stack -bool true')

        self.manager.info('Set the icon size of Dock items to 36 pixels')
        self.manager.exec_cmd('defaults write com.apple.dock tilesize -int 36')

        self.manager.info('Show indicator lights for open applications in the Dock')
        self.manager.exec_cmd('defaults write com.apple.dock show-process-indicators -bool true')

        self.manager.info('Speed up Mission Control animations')
        self.manager.exec_cmd('defaults write com.apple.dock expose-animation-duration -float 0.1')

        self.manager.info('Don\'t group windows by application in Mission Control')
        # (i.e. use the old Expose behavior instead)
        self.manager.exec_cmd('defaults write com.apple.dock expose-group-by-app -bool false')

        self.manager.info('Don\'t automatically rearrange Spaces based on most recent use')
        self.manager.exec_cmd('defaults write com.apple.dock mru-spaces -bool false')

        self.manager.info('Dock hiding setup')
        # Automatically hide and show the Dock
        self.manager.exec_cmd('defaults write com.apple.dock autohide -bool true')
        self.manager.exec_cmd('defaults write com.apple.dock mru-spaces -bool false')
        # Remove the auto-hiding Dock delay
        self.manager.exec_cmd('defaults write com.apple.dock autohide-delay -float 0')
        # Remove the animation when hiding/showing the Dock
        self.manager.exec_cmd('defaults write com.apple.dock autohide-time-modifier -float 0')

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
        self.manager.exec_cmd('defaults write com.apple.dock wvous-tl-corner -int 4')
        self.manager.exec_cmd('defaults write com.apple.dock wvous-tl-modifier -int 0')
        # Top right screen corner -> Mission Control
        self.manager.exec_cmd('defaults write com.apple.dock wvous-tr-corner -int 2')
        self.manager.exec_cmd('defaults write com.apple.dock wvous-tr-modifier -int 0')
        # Bottom right screen corner -> Start screen saver
        self.manager.exec_cmd('defaults write com.apple.dock wvous-br-corner -int 5')
        self.manager.exec_cmd('defaults write com.apple.dock wvous-br-modifier -int 0')

        ###############################################################################
        # Mail
        ###############################################################################
        self.manager.info('Setting email addresses to copy as "foo@example.com" instead of "Foo Bar <foo@example.com>" in Mail.app')
        self.manager.exec_cmd('defaults write com.apple.mail AddressesIncludeNameOnPasteboard -bool false')

        self.manager.info('Display emails in threaded mode, sorted by date (oldest at the top)')
        self.manager.exec_cmd('defaults write com.apple.mail DraftsViewerAttributes -dict-add "DisplayInThreadedMode" -string "yes"')
        self.manager.exec_cmd('defaults write com.apple.mail DraftsViewerAttributes -dict-add "SortedDescending" -string "yes"')
        self.manager.exec_cmd('defaults write com.apple.mail DraftsViewerAttributes -dict-add "SortOrder" -string "received-date"')

        ###############################################################################
        # Terminal
        ###############################################################################
        self.manager.info('Enabling UTF-8 ONLY in Terminal.app and setting the Pro theme by default')
        self.manager.exec_cmd('defaults write com.apple.terminal StringEncodings -array 4')
        self.manager.exec_cmd('defaults write com.apple.Terminal "Default Window Settings" -string "Pro"')
        self.manager.exec_cmd('defaults write com.apple.Terminal "Startup Window Settings" -string "Pro"')

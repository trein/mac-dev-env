from src.core import BaseModule


class Module(BaseModule):
    NAME = 'osx_apps'

    def install(self):
        # Rbenv installation
        self.manager.info('Rbenv installation for managing your rubies')
        self.manager.exec_cmd('brew install rbenv')

        if self.manager.invoke('! grep -qs "rbenv init" ~/.zshrc'):
            self.manager.exec_cmd('printf \'export PATH="$HOME/.rbenv/bin:$PATH"\n\' >> ~/.zshrc')
            self.manager.exec_cmd('printf \'eval "$(rbenv init - --no-rehash)"\n\' >> ~/.zshrc')

            self.manager.info('Enable shims and autocompletion ...')
            self.manager.exec_cmd('eval "$(rbenv init -)')

        self.manager.exec_cmd('export PATH="$HOME/.rbenv/bin:$PATH')

        self.manager.info('Installing rbenv-gem-rehash, we don\'t want to rehash every time we add a gem...')
        self.manager.exec_cmd('brew install rbenv-gem-rehash')

        self.manager.info('Installing ruby-build to install Rubies ...')
        self.manager.exec_cmd('brew install ruby-build')

        # OpenSSL linking
        self.manager.info('Installing and linking OpenSSL...')
        self.manager.exec_cmd('brew install openssl')
        self.manager.exec_cmd('brew link openssl --force')

        # Install ruby latest version
        ruby_version = self.manager.invoke('curl -sSL https://raw.githubusercontent.com/IcaliaLabs/kaishi/master/latest_ruby').strip()

        self.manager.info('Installing Ruby %s' % ruby_version)
        if ruby_version == '2.1.1':
            self.manager.exec_cmd('curl -fsSL https://gist.github.com/mislav/a18b9d7f0dc5b9efc162.txt | rbenv install --patch 2.1.1')
        else:
            self.manager.exec_cmd('rbenv install %s' % ruby_version)

        self.manager.info('Set ruby version %s as the default' % ruby_version)
        self.manager.exec_cmd('rbenv global "%s"' % ruby_version)
        self.manager.exec_cmd('rbenv rehash')

        self.manager.info('Updating gems...')
        self.manager.exec_cmd('gem update --system')

        self.manager.info('Setup gemrc for default options')
        if self.manager.invoke('[ ! -f ~/.gemrc ]'):
            self.manager.exec_cmd('printf \'gem: --no-document\' >> ~/.gemrc')

        # Bundler installation
        self.manager.info('Installing bundler...')
        self.manager.exec_cmd('gem install bundler')

        number_of_cores = int(self.manager.invoke('sysctl -n hw.ncpu')) - 1
        self.manager.info('Optimizing Bundler. Setting max cores to %s...' % number_of_cores)
        self.manager.exec_cmd('bundle config --global jobs %s' % number_of_cores)

        self.manager.info('Installing Foreman...')
        self.manager.exec_cmd('gem install foreman')

        self.manager.info('Installing Rails...finally!')
        self.manager.exec_cmd('gem install rails')

        self.manager.info('Installing mailcatcher gem...!')
        self.manager.exec_cmd('gem install mailcatcher')

        self.manager.info('Installing the heroku toolbelt...')
        self.manager.exec_cmd('brew install heroku-toolbelt')

        self.manager.info('Installing custom Rails app generator from Icalia')
        self.manager.exec_cmd('curl -L https://raw2.github.com/IcaliaLabs/railsAppCustomGenerator/master/install.sh | sh')

        self.manager.info('Installing pow to serve local rails apps like a superhero...')
        self.manager.exec_cmd('curl get.pow.cx | sh')

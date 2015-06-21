from bin import *


def install():
    # Rbenv installation
    info('Rbenv installation for managing your rubies')
    exec_cmd('brew install rbenv')

    if invoke('! grep -qs "rbenv init" ~/.zshrc'):
        exec_cmd('printf \'export PATH="$HOME/.rbenv/bin:$PATH"\n\' >> ~/.zshrc')
        exec_cmd('printf \'eval "$(rbenv init - --no-rehash)"\n\' >> ~/.zshrc')

        info('Enable shims and autocompletion ...')
        exec_cmd('eval "$(rbenv init -)')

    exec_cmd('export PATH="$HOME/.rbenv/bin:$PATH')

    info('Installing rbenv-gem-rehash, we don\'t want to rehash every time we add a gem...')
    exec_cmd('brew install rbenv-gem-rehash')

    info('Installing ruby-build to install Rubies ...')
    exec_cmd('brew install ruby-build')

    # OpenSSL linking
    info('Installing and linking OpenSSL...')
    exec_cmd('brew install openssl')
    exec_cmd('brew link openssl --force')

    # Install ruby latest version
    ruby_version = invoke('curl -sSL https://raw.githubusercontent.com/IcaliaLabs/kaishi/master/latest_ruby').strip()

    info('Installing Ruby %s' % ruby_version)
    if ruby_version == '2.1.1':
        exec_cmd('curl -fsSL https://gist.github.com/mislav/a18b9d7f0dc5b9efc162.txt | rbenv install --patch 2.1.1')
    else:
        exec_cmd('rbenv install %s' % ruby_version)

    info('Set ruby version %s as the default' % ruby_version)
    exec_cmd('rbenv global "%s"' % ruby_version)
    exec_cmd('rbenv rehash')

    info('Updating gems...')
    exec_cmd('gem update --system')

    info('Setup gemrc for default options')
    if invoke('[ ! -f ~/.gemrc ]'):
        exec_cmd('printf \'gem: --no-document\' >> ~/.gemrc')

    # Bundler installation
    info('Installing bundler...')
    exec_cmd('gem install bundler')

    number_of_cores = int(invoke('sysctl -n hw.ncpu')) - 1
    info('Optimizing Bundler. Setting max cores to %s...' % number_of_cores)
    exec_cmd('bundle config --global jobs %s' % number_of_cores)

    info('Installing Foreman...')
    exec_cmd('gem install foreman')

    info('Installing Rails...finally!')
    exec_cmd('gem install rails')

    info('Installing mailcatcher gem...!')
    exec_cmd('gem install mailcatcher')

    info('Installing the heroku toolbelt...')
    exec_cmd('brew install heroku-toolbelt')

    info('Installing custom Rails app generator from Icalia')
    exec_cmd('curl -L https://raw2.github.com/IcaliaLabs/railsAppCustomGenerator/master/install.sh | sh')

    info('Installing pow to serve local rails apps like a superhero...')
    exec_cmd('curl get.pow.cx | sh')

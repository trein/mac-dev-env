#!/bin/sh
###############################################################################
# Ruby tools
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

# Rbenv installation
pretty_print "Rbenv installation for managing your rubies"
  brew install rbenv

if ! grep -qs "rbenv init" ~/.zshrc; then
  printf 'export PATH="$HOME/.rbenv/bin:$PATH"\n' >> ~/.zshrc
  printf 'eval "$(rbenv init - --no-rehash)"\n' >> ~/.zshrc

  pretty_print "Enable shims and autocompletion ..."
    eval "$(rbenv init -)"
fi


export PATH="$HOME/.rbenv/bin:$PATH"

pretty_print "Installing rbenv-gem-rehash, we don't want to rehash every time we add a gem..."
  brew install rbenv-gem-rehash

pretty_print "Installing ruby-build to install Rubies ..."
  brew install ruby-build

# OpenSSL linking
pretty_print "Installing and linking OpenSSL..."
brew install openssl
brew link openssl --force

# Install ruby latest version
ruby_version="$(curl -sSL https://raw.githubusercontent.com/IcaliaLabs/kaishi/master/latest_ruby)"

pretty_print "Installing Ruby $ruby_version"
  if [ "$ruby_version" = "2.1.1" ]; then
    curl -fsSL https://gist.github.com/mislav/a18b9d7f0dc5b9efc162.txt | rbenv install --patch 2.1.1
  else
    rbenv install "$ruby_version"
  fi

  pretty_print "Set ruby version $ruby_version as the default"

  rbenv global "$ruby_version"
  rbenv rehash

pretty_print "Updating gems..."
  gem update --system

pretty_print "Setup gemrc for default options"
  if [ ! -f ~/.gemrc ]; then
    printf 'gem: --no-document' >> ~/.gemrc
  fi

# Bundler installation
pretty_print "Installing bundler..."
  gem install bundler
#
pretty_print "Optimizing Bundler..."
  number_of_cores=$(sysctl -n hw.ncpu)
  bundle config --global jobs $((number_of_cores - 1))

pretty_print "Installing Foreman..."
  gem install foreman

pretty_print "Installing Rails...finally!"
  gem install rails

pretty_print "Installing mailcatcher gem...!"
  gem install mailcatcher

pretty_print "Installing the heroku toolbelt..."
  brew install heroku-toolbelt

pretty_print "Installing custom Rails app generator from Icalia"
  curl -L https://raw2.github.com/IcaliaLabs/railsAppCustomGenerator/master/install.sh | sh

pretty_print "Installing pow to serve local rails apps like a superhero..."
  curl get.pow.cx | sh
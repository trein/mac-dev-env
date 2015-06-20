#!/bin/sh
###############################################################################
# Installing VIM customizations
###############################################################################
pretty_print() {
  printf "\n%b\n" "$1"
}

pretty_print "Installing pathogen..."
mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

pretty_print "Installing vim-sensible..."
cd ~/.vim/bundle && git clone git://github.com/tpope/vim-sensible.git
cd -1

pretty_print "Installing vim-nerdtree..."
cd ~/.vim/bundle && git clone https://github.com/scrooloose/nerdtree
cd -1

pretty_print "Installing vim-ctrlp..."
cd ~/.vim/bundle && git clone https://github.com/kien/ctrlp.vim
cd -1

pretty_print "Installing vim-airline..."
cd ~/.vim/bundle && git clone https://github.com/bling/vim-airline
cd -1

pretty_print "Installing vim-colors-solarized..."
cd ~/.vim/bundle && git clone https://github.com/altercation/vim-colors-solarized
cd -1

pretty_print "Installing vim-syntastic..."
cd ~/.vim/bundle && git clone https://github.com/scrooloose/syntastic
cd -1
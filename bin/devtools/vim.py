from bin import *


def install():
    info('Installing pathogen...')
    exec_cmd('mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim')

    info('Installing vim-sensible...')
    exec_cmd('cd ~/.vim/bundle && git clone git://github.com/tpope/vim-sensible.git')
    exec_cmd('cd -1')

    info('Installing vim-nerdtree...')
    exec_cmd('cd ~/.vim/bundle && git clone https://github.com/scrooloose/nerdtree')
    exec_cmd('cd -1')

    info('Installing vim-ctrlp...')
    exec_cmd('cd ~/.vim/bundle && git clone https://github.com/kien/ctrlp.vim')
    exec_cmd('cd -1')

    info('Installing vim-airline...')
    exec_cmd('cd ~/.vim/bundle && git clone https://github.com/bling/vim-airline')
    exec_cmd('cd -1')

    info('Installing vim-colors-solarized...')
    exec_cmd('cd ~/.vim/bundle && git clone https://github.com/altercation/vim-colors-solarized')
    exec_cmd('cd -1')

    info('Installing vim-syntastic...')
    exec_cmd('cd ~/.vim/bundle && git clone https://github.com/scrooloose/syntastic')
    exec_cmd('cd -1')

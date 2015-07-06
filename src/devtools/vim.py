from src.core import BaseModule


class Module(BaseModule):
    NAME = 'devtools_vim'

    def install(self):
        self.manager.info('Installing pathogen...')
        self.manager.exec_cmd('mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim')

        self.manager.info('Installing vim-sensible...')
        self.manager.exec_cmd('cd ~/.vim/bundle && git clone git://github.com/tpope/vim-sensible.git')
        self.manager.exec_cmd('cd -1')

        self.manager.info('Installing vim-nerdtree...')
        self.manager.exec_cmd('cd ~/.vim/bundle && git clone https://github.com/scrooloose/nerdtree')
        self.manager.exec_cmd('cd -1')

        self.manager.info('Installing vim-ctrlp...')
        self.manager.exec_cmd('cd ~/.vim/bundle && git clone https://github.com/kien/ctrlp.vim')
        self.manager.exec_cmd('cd -1')

        self.manager.info('Installing vim-airline...')
        self.manager.exec_cmd('cd ~/.vim/bundle && git clone https://github.com/bling/vim-airline')
        self.manager.exec_cmd('cd -1')

        self.manager.info('Installing vim-colors-solarized...')
        self.manager.exec_cmd('cd ~/.vim/bundle && git clone https://github.com/altercation/vim-colors-solarized')
        self.manager.exec_cmd('cd -1')

        self.manager.info('Installing vim-syntastic...')
        self.manager.exec_cmd('cd ~/.vim/bundle && git clone https://github.com/scrooloose/syntastic')
        self.manager.exec_cmd('cd -1')

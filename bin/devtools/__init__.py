from bin import *
import tools
import apps
import dbs
import vim
import python
import ruby
import node


def install():
    # Tools
    header('Installing dev tools...', 1)
    tools.install()
    display()

    # VIM
    header('Installing VIM extensions...', 1)
    vim.install()
    display()

    # Apps
    header('Installing dev apps...', 1)
    apps.install()
    display()

    # Databases
    header('Installing dev databases...', 1)
    dbs.install()
    display()

    # NodeJS
    header('Installing NodeJS...', 1)
    node.install()
    display()

    # Python
    header('Installing Python...', 1)
    python.install()
    display()

    # Ruby
    header('Installing Ruby...', 1)
    ruby.install()
    display()

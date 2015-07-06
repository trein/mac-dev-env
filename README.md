MDE (mac-dev-env)
=================

## Executing

Before executing the script, please read through it and understand what it is doing.

Executing script with Python.

	$ python init.py
    usage: init.py [-h] [-d] [-v] [-m MODULES [MODULES ...]]

    Setup an ideal mac development environment on a fresh install of OS X Yosemite

    optional arguments:
      -h, --help            show this help message and exit
      -d, --d               debug run (default false)
      -v, --verbose         verbose output (default false)
      -m MODULES [MODULES ...], --modules MODULES [MODULES ...]
                            modules to install (default all)

---

## General Notes
We assume you are on a fresh install of Yosemite. If you already have an environment setup, don't run `init.py` script. Instead, go over the script and cherry pick what you need.

Mac Dev Env Setup consists of a collection of essential applications and development tools. It also sets up several preferences and custom settings on OS X.

## What does it install?

### System preferences
* Name of computer
* General preferences (Finder, Mail, etc)
* Mouse/trackpad and keyboard settings
* Mission Control and Hot Corners
* Essential applications and package manager (Homebrew)

### Development tools
* Apple development tools: `$ xcode-select --install`
* VIM customizations
* Linux tools
* Enhanced shell and terminal emulator
* Databases
* Version control
* Programming languages and platforms (Python, Ruby, NodeJS)
* Development applications and IDE's

import argparse
import src.main
import logging


def main():    
    parser = argparse.ArgumentParser(description='Setup an ideal mac development environment on a fresh install of OS X Yosemite')
    parser.add_argument('-d', '--d', dest='debug', action='store_true', default=False, help='debug run (default false)')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='verbose output (default false)')
    parser.add_argument('-m', '--modules', dest='modules', action='store', nargs='+', default=None, help='modules to install (default all)')
    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    log_format = '%(asctime)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)
    logger = logging.getLogger(__name__)

    logger.debug('Initializing installer...')
    logger.debug('Received arguments [%s]' % args)
    logger.debug('Running installer...')
    src.main.Installer(args).start()


if __name__ == '__main__':
    main()
#/usr/bin/env python

VERSION = (0, 1, 1, "alpha")

__author__    = 'Mike Taylor'
__contact__   = 'bear@bear.im'
__copyright__ = 'Copyright (c) 2014 by Mike Taylor'
__license__   = 'MIT'
__version__   = '.'.join(map(str, VERSION[0:3])) + ''.join(VERSION[3:])

from tools import mkpath, findFile, normalizeFilename, loadConfig
from site import Site, Post

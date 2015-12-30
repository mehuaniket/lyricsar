#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib import filetest
from .tinytag import TinyTag, TinyTagException, ID3, Ogg, Wave, Flac
from filetest import filetest

__version__ = '0.10.1'

if __name__ == '__main__':
    print(TinyTag.get(sys.argv[1]))

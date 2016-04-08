#!/usr/bin/env python

import sys
import string
from lyricsar import plugin,google
from lyricsar.setting import PLUGIN


def main(argv):
#===========================[LOAD GOOGLE PLUGIN]================================
    if len(argv)>1:
        title=sys.argv[1]
        lyricsite=google.getLinkUrl(title)
        print lyricsite
#===============================================================================
        for web in PLUGIN:
            find=string.find(lyricsite,web)
            if find>-1:
                getby= web
        if getby=="lyricsmint":
            print plugin.get_lyricsmint(lyricsite)
        elif getby=="azlyrics":
            print plugin.get_azlyrics(lyricsite)
        else:
            print "plugin is not available for website"





#if no parameter is received from terminal
    else:
        print "usage of lyrics.py\n $ lyrics.py [title of the song]"
#===============================================================================

if __name__ == '__main__': sys.exit(main(sys.argv))

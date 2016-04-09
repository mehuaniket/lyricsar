#!/usr/bin/env python

import sys
import string
from lyricsar import plugin,google
from lyricsar.setting import PLUGIN
import os
import subprocess

def main(argv):
#===========================[LOAD GOOGLE PLUGIN]================================
    if len(argv)>1:
        if sys.argv[1]=="play":
            os.system("rhythmbox-client --play &")

        elif sys.argv[1]=="pause":
            os.system("rhythmbox-client --pause")

        elif sys.argv[1]=="next":
            os.system("rhythmbox-client --next")

        elif sys.argv[1]=="playinfo":
            os.system("rhythmbox-client --print-playing")

        elif sys.argv[1]=="playtitle":
            os.system("rhythmbox-client --print-playing-format=%tt")

        elif sys.argv[1]=="playlyrics":
            title= os.popen("rhythmbox-client --print-playing-format=%tt").read()
            # title=subprocess.check_output(["rhythmbox-client","--print-playing-format=%tt"])
            # proc = subprocess.Popen("rhythmbox-client --print-playing-format=%tt", stdout=subprocess.PIPE)
            # title = proc.stdout.read()
            lyricsite=google.getLinkUrl(title)
            print lyricsite
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

        else:
            getby="none"
            title=sys.argv[1]
            lyricsite=google.getLinkUrl(title)
            print lyricsite
            for web in PLUGIN:
                find=string.find(lyricsite,web)
                if find>-1:
                    getby= web
            if getby=="lyricsmint":
                print plugin.get_lyricsmint(lyricsite)
            elif getby=="azlyrics":
                print plugin.get_azlyrics(lyricsite)
            elif getby=="none":
                print "plugin is not available for website"





#if no parameter is received from terminal
    else:
        print "usage of lyrics.py\n\n $ lyrics.py [title of the song] or [OPTIONS]\n"
        print "FOLLOWING IS OPTIONS:\n"
        print "playlyrics\n\tprint lyrics of song that is now playing on player\n"
        print "next \n\tto play next song\n"
        print "pause\n\tto pause a song\n"
        print "play\n\tto play song or start rhythmbox aplication in background\n"
        print "playinfo\n\tto print information of song that you playing in music player\n"

#===============================================================================

if __name__ == '__main__': sys.exit(main(sys.argv))

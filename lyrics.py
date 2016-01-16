#!c:\Python27\python.EXE
import sys
import string
from lyricsar import *
from lyricsar.plugin import *
import  lyricsar.config
def main(argv):
    #===============================================================================
    #load available plugin from plugin.conf
    plugin=config.PLUGIN
    #===============================================================================

    #=================================class init====================================
    #this class have function that can process string object in way we need
    sp=strprocess.strprocess()
    #pagegetter class that used when we want to work with INTERNET-PAGE_UP_DOWN
    pg=pagegetter.pagegetter()

    #===============================================================================

    #============================plugin class init==================================
    #following lines are process the title and make it song name to pass pluginclass
    #title=tag.title
    if len(argv)>1:
        title=sys.argv[1]
        title=sp.addplus(title)

        #initialize lyricsmint class that used to process page and get lyrics .
        lm=google.google(title)

        #===============================================================================

        #==============================provide search URL===============================
        search_link=lm.get_search()
        print search_link

        url_plug="lyricsmint"
        #===============================================================================
        #============================load object on fly=================================
        for URL in plugin:
            find=string.find(search_link,URL)
            if find>-1:
                url_plug=URL
                break;


        #=======================load compatible module on the fly=======================
        creator="gm="+url_plug+"."+url_plug+"('"+title+"')"
        print creator
        exec(creator)
        #===============================================================================

        #===============================================================================
        #this block is get lyrics from INTERNET
        search_page=pg.get_pagedata(search_link)
        link=gm.get_link(search_page)
        print link
        lyrics_page=pg.get_pagedata(link)
        lyrics=gm.get_lyrics(lyrics_page)
        lyrics=sp.removeHTML(lyrics)
        print lyrics
    else:
        print "usage of lyrics.py\n $ lyrics.py [title of the song]"
    #===============================================================================

if __name__ == '__main__': sys.exit(main(sys.argv))



#=======================:information about tags:================================
# album= tag.album                       # album as string
# artist=tag.artist                      # artist name as string
# audio_offset= tag.audio_offset         # number of bytebefore audio databegins
# bitrate= tag.bitrate                   # bitrate in kBits/s
# duration=tag.duration                  # duration of the song in seconds
# filesize=tag.filesize                  #file size in bytes
# genre=tag.genre                        # genre as string
# samlerate=tag.samplerate               # samples per second
# title=tag.title                        # title of the song
# track=tag.track                        # track number as string
# track_total= tag.track_total           # total number of tracks as string
# year=tag.year                          # year or data as string
#===============================================================================

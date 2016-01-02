from plugin import lyricsmint
from lib import tinytag
from lib import strprocess
from lib import pagegetter
from lib import filetest
import sys

#first i would like to that this project is in development phase and that's why
#i make block with comment tag in specific way that give a information about
# lines of code inside



#=================================class init====================================
#this class have function that can process string object in way we need
sp=strprocess.strprocess()
#pagegetter class that used when we want to work with INTERNET-PAGE_UP_DOWN
pg=pagegetter.pagegetter()

#===============================================================================

#============================plugin class init==================================
#following lines are process the title and make it song name to pass pluginclass
#title=tag.title
title=sys.argv[1]
print title
#initialize lyricsmint class that used to process page and get lyrics .
lm=lyricsmint.lyricsmint(title)

#===============================================================================

#==============================provide search URL===============================
search_link=lm.get_search()
print search_link
#===============================================================================


#===============================================================================
#this block is get lyrics from INTERNET
search_page=pg.get_pagedata(search_link)
link=lm.get_link(search_page)
print link
lyrics_page=pg.get_pagedata(link)
lyrics=lm.get_lyrics(lyrics_page)
lyrics=sp.removeHTML(lyrics)
print lyrics
#===============================================================================



#===============================================================================
#this whole bunch of line only for offline testing for module

# file_test1=filetest.filetest("test\Search results for tum hi ho.html")
#
# file_test2=filetest.filetest("test\MERI AASHIQUI LYRICS - Aashiqui 2.html")
#
#
# link=lm.get_link(file_test1.read())
# print link
# lyrics=lm.get_lyrics(file_test2.read())
# lyrics=sp.removeHTML(lyrics)
# print lyrics

#===============================================================================

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

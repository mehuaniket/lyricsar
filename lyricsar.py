from plugin import lyricsmint
from lib import tinytag
from lib import strprocess
from lib import pagegetter
from lib import filetest

tag = tinytag.TinyTag.get('music\meherbaan.mp3',image=True)

file_test1=filetest.filetest("test\Search results for tum hi ho.html")

file_test2=filetest.filetest("test\MERI AASHIQUI LYRICS - Aashiqui 2.html")



title=tag.title
sp=strprocess.strprocess()
title=sp.removemarks(title).split()[0]
lm=lyricsmint.lyricsmint(title,tag)
search_link=lm.get_search()
print search_link
pg=pagegetter.pagegetter()
page=pg.get_pagedata(search_link)
link=lm.get_link(file_test1.read())
#page=pg.get_pagedata(file_test2.read())

lyrics=lm.get_lyrics(file_test2.read())
lyrics=sp.removeHTML(lyrics)
print lyrics



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

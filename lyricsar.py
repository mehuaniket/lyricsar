import tinytag
import string
from filetest import filetest
from htmldom import HtmlDom
from bs4 import BeautifulSoup
from process import process

tag = tinytag.TinyTag.get('music\meherbaan.mp3',image=True)

print tag

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


tit=tag.title.split()
print tit
search="http://www.lyricsmint.com/search?q="+tit[0]
print search

#initialize filetest class to test other file handling function
file_test=filetest("test\Search results for tum hi ho.html")
#print file_test.read()

html_doc=file_test.read()
#dom = HtmlDom().createDom(file_test.read())
# elem = dom.find( 'blog-posts hfeed' )
# a = dom.find( 'a' )
# for link in a:
#     print( link.attr( "href" ) )
links=[]
soup = BeautifulSoup(html_doc, 'html.parser')
#=================in html testing =============================================
# post=soup.find_all("div", class_="post-title")
#     #inks=BeautifulSoup(post, 'html.parser')
#     #for link in links.find_all('a'):
#     #    print(link.get('href'))
#
# link= post[1].find_all("a")
# print (link[0].get('href'))
# #pro=process()
# #htmllink=pro.makehtml(post[1])
# #links = BeautifulSoup(post[1], 'html.parser')
# #print links.find_all("a")
#===============================================================================
post=soup.find_all("div", class_="post-title")
for block in post:
    linklist=block.find_all("a")
    if len(linklist)>0:
        link=linklist[0].get('href')
        print link



# songlyric=soup.find_all("div", id="lyric")
# lyrics= songlyric[0].find_all("p")
# print lyrics[0]

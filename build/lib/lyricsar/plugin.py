from bs4 import BeautifulSoup
#from filetest import filetest
import string
import sys


class lyricsmint:
    """ this plugin provide lyrics from lyricsmint.com"""
    def __init__(self,title):
        self.search_url="http://www.lyricsmint.com/search?q="
        self.title=title
        print self.title

    def get_search(self):
        """get_search function make a url from title and url"""
        url=self.search_url+self.title
        return str(url)

    def get_link(self,searchpage):
        """get_link received a searchpage page that fetch page from url provide
         by do_search ,and give user a link of page that have lyrics """

        if searchpage=="URL error":
            return "no links"
        html_search=searchpage
        self.search = BeautifulSoup(html_search, 'html.parser')
        post=self.search.find_all("div", class_="post-title")
        for block in post:
            linklist=block.find_all("a")
            if len(linklist)>0:
                return str(linklist[0].get('href'))


    def get_lyrics(self,lyricspage):
        if lyricspage=="URL error":
            return "no lyrics"
        """ get_lyrics received a lyricspagepage that fetch fro url provide by
        get_link ,and give user a lyrics user wish"""
        html_lyrics=lyricspage
        self.soup = BeautifulSoup(html_lyrics, 'html.parser')
        songlyric=self.soup.find_all("div", id="lyric")
        self.lyrics= songlyric[0].find_all("p")
        return str(self.lyrics[0])





#================================ tesing =======================================
if __name__=="__main__":
    # tag={'album': u'Bang Bang - Single',
    #      'audio_offset': 116354,
    #      'artist': u'Ash King, Shilpa Rao & Shekhar Ravjiani',
    #      'track': None,
    #      'title': u'Meherbaan - Bang Bang - WapKing.Cc',
    #      'track_total': None,
    #      'channels': 2,
    #      'genre': u'Bollywood',
    #      'filesize': 5025278,
    #      'year': u'2014',
    #      'duration': 307.5054509861498,
    #      'samplerate': 44100,
    #      'bitrate': 128}
    lyrics_mint=lyricsmint("meherbaan")
    file_test=filetest("test\lyricsmint\Search results for tum hi ho.html")
    print lyrics_mint.get_search()
    file=file_test.read()
    print lyrics_mint.get_link(file)
    file_test=filetest("test\lyricsmint\MERI AASHIQUI LYRICS - Aashiqui 2.html")
    file=file_test.read()
    lyric=lyrics_mint.get_lyrics(file)
    lyric=string.replace(lyric,"<br>"," ")
    lyric=string.replace(lyric,"</br>"," ")
    lyric=string.replace(lyric,"<p>"," ")
    lyric=string.replace(lyric,"</p>"," ")
    print lyric

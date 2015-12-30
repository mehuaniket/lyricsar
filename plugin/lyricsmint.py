from bs4 import BeautifulSoup
from filetest import filetest
class lyricsmint:
    """ this plugin provide lyrics from lyricsmint.com"""
    def __init__(self,songtag):
        self.tag=songtag
        self.search_url="http://www.lyricsmint.com/search?q="


    def do_search(self):
        """do_search function make a url from title and url"""
        self.title=tag['title'].split()
        url=self.search_url+self.title[0]
        return url

    def get_link(self,searchpage):
        """get_link received a searchpage page that fetch from url provide by
        do_search ,and give user a link of page that have lyrics """
        html_search=searchpage
        self.search = BeautifulSoup(html_search, 'html.parser')
        post=self.search.find_all("div", class_="post-title")
        for block in post:
            linklist=block.find_all("a")
            if len(linklist)>0:
                return linklist[0].get('href')


    def get_lyrics(self,lyricspage):
        """ get_lyrics received a lyricspagepage that fetch fro url provide by
        get_link ,and give user a lyrics user wish"""
        html_lyrics=lyricspage
        self.soup = BeautifulSoup(html_lyrics, 'html.parser')
        songlyric=self.soup.find_all("div", id="lyric")
        self.lyrics= songlyric[0].find_all("p")
        return self.lyrics[0]






#================================ tesing =======================================
if __name__=="__main__":
    tag={'album': u'Bang Bang - Single',
         'audio_offset': 116354,
         'artist': u'Ash King, Shilpa Rao & Shekhar Ravjiani',
         'track': None,
         'title': u'Meherbaan - Bang Bang - WapKing.Cc',
         'track_total': None,
         'channels': 2,
         'genre': u'Bollywood',
         'filesize': 5025278,
         'year': u'2014',
         'duration': 307.5054509861498,
         'samplerate': 44100,
         'bitrate': 128}
    lyrics_mint=lyricsmint(tag)
    file_test=filetest("test\Search results for tum hi ho.html")
    print lyrics_mint.do_search()
    file=file_test.read()
    print lyrics_mint.get_link(file)
    file_test=filetest("test\MERI AASHIQUI LYRICS - Aashiqui 2.html")
    file=file_test.read()
    print lyrics_mint.get_lyrics(file)

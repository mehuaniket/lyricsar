from bs4 import BeautifulSoup
import string
import sys
from setting import LYRICSMINT_URL

class lyricsmint:
    """ this plugin provide lyrics from lyricsmint.com"""
    def __init__(self,title):
        self.search_url=LYRICSMINT_URL
        self.title=title

    def get_search(self):
        """get_search function make a url from title and url"""
        url=self.search_url+self.title
        return str(url)

    def get_link(self,searchpage):
        """get_link received a searchpage page that fetch page from url provide
         by do_search ,and give user a link of page that have lyrics """

        html_search=searchpage
        self.search = BeautifulSoup(html_search, 'html.parser')
        post=self.search.find_all("div", class_="post-title")
        for block in post:
            linklist=block.find_all("a")
            if len(linklist)>0:
                return str(linklist[0].get('href'))


    def get_lyrics(self,lyricspage):
        """ get_lyrics received a lyricspagepage that fetch fro url provide by
        get_link ,and give user a lyrics user wish"""

        html_lyrics=lyricspage
        self.soup = BeautifulSoup(html_lyrics, 'html.parser')
        songlyric=self.soup.find_all("div", id="lyric")
        self.lyrics= songlyric[0].find_all("p")
        return str(self.lyrics[0])





#================================ tesing =======================================
if __name__=="__main__":

    lyrics_mint=lyricsmint("meherbaan")

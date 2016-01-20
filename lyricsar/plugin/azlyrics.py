from bs4 import BeautifulSoup
import string
import sys
from setting import azlyrics_URL
import urllib2
from lyricsar import strprocess
class azlyrics:
    """ this plugin provide lyrics from azlyrics.com"""
    def __init__(self,title):
        self.search_url=azlyrics_URL
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
        post=self.search.find_all("div")
        for block in post:
            linklist=block.find_all("a")
            if len(linklist)>0:
                return str(linklist[0].get('href'))


    def get_lyrics(self,lyricspage):
        """ get_lyrics received a lyricspagepage that fetch fro url provide by
        get_link ,and give user a lyrics user wish"""

        html_lyrics=lyricspage
        self.soup = BeautifulSoup(html_lyrics, 'html.parser')
        songlyric=self.soup.find_all("div" ,class_=None)
        soup = BeautifulSoup(str(songlyric[1]), 'html.parser')
        return str(soup.get_text())






#================================ testing =======================================
if __name__=="__main__":
        sp=strprocess.strprocess()
        azly=azlyrics("imfreak+lyrics")
        url="http://www.azlyrics.com/lyrics/justinbieber/baby.html"
        request=urllib2.Request(url,None,{'Referer':'www.lyricsmint.com'})
        proxy = urllib2.ProxyHandler({'http': 'http://mh514uvamp1-16:1434@10.0.0.5:8080'})
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        lyricpage=urllib2.urlopen(request)
        lyrcweb=azly.get_lyrics(lyricpage)
        print lyrcweb

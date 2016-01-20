from bs4 import BeautifulSoup
import string
import sys
from setting import LYRICSMINT_URL
from lyricsar import strprocess
import urllib2
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
        self.lyric=""
        html_lyrics=lyricspage
        self.soup = BeautifulSoup(html_lyrics, 'html.parser')
        songlyric=self.soup.find_all("div", id="lyric")
        self.lyrics= songlyric[0].find_all("p")
        print type(self.lyrics)






#================================ tesing =======================================
if __name__=="__main__":
    sp=strprocess.strprocess()
    lyrc=lyricsmint("imfreak+lyrics")
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    url="http://www.lyricsmint.com/2014/09/meherbaan-bang-bang.html"
    request=urllib2.Request(url,None,headers)
    proxy = urllib2.ProxyHandler({'http': 'http://mh514uvamp1-16:1434@10.0.0.5:8080'})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    lyricpage=urllib2.urlopen(request)
    lyrcweb=lyrc.get_lyrics(lyricpage)
    print lyrcweb
    lyricweb=sp.removeHTML(lyrcweb)
    print lyricweb

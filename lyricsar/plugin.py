from bs4 import BeautifulSoup
import string
import sys
from setting import proxy_enable,proxy_url
import urllib2
import mechanize

def get_lyricsmint(url):
    """ get_lyrics received a lyricspagepage that fetch fro url provide by
    get_link ,and give user a lyrics user wish"""
    lyric=""

    if(proxy_enable):
        proxy = urllib2.ProxyHandler({'http':proxy_url})
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    req = urllib2.urlopen(req)
    html_lyrics = req.read()
    soup = BeautifulSoup(html_lyrics, 'html.parser')
    songlyric=soup.find_all("div", id="lyric")
    # lyrics= str(songlyric[0].find_all("p"))
    lyrics=""
    for phase in songlyric[0].find_all("p"):
        lyrics=lyrics+str(phase)+"\n"
    lyrics=lyrics.replace("</p>","\n")
    lyrics=lyrics.replace("<br/>","\n")
    return BeautifulSoup(lyrics).text

def get_azlyrics(url):
        """ get_lyrics received a lyricspagepage that fetch fro url provide by
        get_link ,and give user a lyrics user wish"""

        lyric=""
        if(proxy_enable):
            proxy = urllib2.ProxyHandler({'http':proxy_url})
            auth = urllib2.HTTPBasicAuthHandler()
            opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
        req = urllib2.urlopen(url)
        html_lyrics = req.read()
        soup = BeautifulSoup(html_lyrics, 'html.parser')
        songlyric=soup.find_all("div" ,class_=None)
        soup = BeautifulSoup(str(songlyric[1]), 'html.parser')
        return soup.get_text()

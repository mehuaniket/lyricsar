
import string
import sys
import urllib2
import simplejson
import httplib
from bs4 import BeautifulSoup
from setting import GOOGLE_API_URL
from lyricsar.errorlist import errorlist
class google:
    response=""
    """ this plugin provide link by traverse results of google.com with extra keyword"""
    def __init__(self,title):
        self.search_url=GOOGLE_API_URL
        self.title=title

    def get_search(self):
        """get_search function make a url from title and url"""
        string.replace(self.title," ","%20")
        url=self.search_url+self.title
        return str(url)

    def get_link(self,searchpage):
        """get_link fetch first link from google results """
        try:
            results = simplejson.load(searchpage)
            print results
            return results
        except:
            sys.exit(errorlist['0e02'])

#================================ tesing =======================================
if __name__ =="__main__":

    gogle=google("meherbaan+lyrics")
    url=gogle.get_search()
    request=urllib2.Request(url,None,{'Referer':'www.lyricsmint.com'})
    print url
    proxy = urllib2.ProxyHandler({'http': 'http://mh514uvamp1-16:1434@10.0.0.5:8080'})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    searchpage=urllib2.urlopen(request)
    print searchpage
    lyrcweb=gogle.get_link(searchpage)
    print lyrcweb

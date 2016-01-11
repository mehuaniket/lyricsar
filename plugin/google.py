from bs4 import BeautifulSoup
import string
import sys
from setting import GOOGLE_API_URL
import urllib2
import simplejson


class google:
    """ this plugin provide link by traverse results of google.com with extra keyword"""
    def __init__(self,title):
        self.search_url=GOOGLE_API_URL
        self.title=title

    def get_search(self):
        """get_search function make a url from title and url"""
        string.replace(self.title," ","%20")
        url=self.search_url+self.title
        print url
        return str(url)

    def get_link(self,url):
        """get_link fetch first link from google results """
        try:
            try:
                response = urllib2.urlopen(url)
            finally:
                print "INTERNET IS NOT AVAILABLE"

                # Process the JSON string.
                results = simplejson.load(response)
                # now have some fun with the results...
                return results
        finally:
            print "FAILED TO LOAD JSON"





#================================ tesing =======================================
if __name__=="__main__":

    gogle=google("meherbaan")
    url=gogle.get_search()
    json=gogle.get_link(url)

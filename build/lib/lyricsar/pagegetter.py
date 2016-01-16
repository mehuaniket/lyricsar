
import urllib2
import sys
from errorlist import errorlist
class pagegetter:
   """provide html data or other internet things on the request"""
   def __init__(self):
       self.url = ''
       self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
       self.headers = { 'User-Agent' : self.user_agent }
   def get_pagedata(self,url):
       try:
           self.url=url
           req = urllib2.urlopen(self.url)
           the_page = req.read()
           return the_page

       except:
           sys.exit(errorlist['0e01'])






#===================================testing====================================
if __name__=="__main__":
    pageget=pagegetter()
    url="http://www.lyricsmint.com/2013/03/tum-hi-ho-aashiqui-2.html"
    print pageget.get_pagedata(url)

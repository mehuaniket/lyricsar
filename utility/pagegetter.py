
import urllib2
import sys
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
           #response = urllib2.urlopen(req)
           the_page = req.read()
           return the_page
       except(urllib2.URLError,urllib2.HTTPErrorProcessor):
           return  "URL error"
       except:
           return "URL error" 






#===================================testing====================================
if __name__=="__main__":
    pageget=pagegetter()
    url="http://www.lyricsmint.com/2013/03/tum-hi-ho-aashiqui-2.html"
    print pageget.get_pagedata(url)

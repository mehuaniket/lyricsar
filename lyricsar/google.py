import json
from setting import GOOGLE_API_URL,proxy_enable,proxy_url
import urllib2

def getLinkUrl(search):
    search=search.replace(" ","%20")
    url=GOOGLE_API_URL+"%20lyrics"+search
    if(proxy_enable):
        proxy = urllib2.ProxyHandler({'http':proxy_url})
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    try:
        req = urllib2.urlopen(url)
        json_page = req.read()
        srch_dic=json.loads(json_page)
    except urllib2.URLError:
        print "ERROR:internet is not available"

    try:
        url=srch_dic['responseData']['results'][0]['url']
    except IndexError:
        print "ERROR:search string is not perfect"
    except UnboundLocalError:
        print "ERROR:search data is not received"

    return url

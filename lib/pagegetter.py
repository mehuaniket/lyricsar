import urllib
import urllib2

url = ''
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

headers = { 'User-Agent' : user_agent }

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()

import pycurl
 
c = pycurl.Curl()
c.setopt(c.URL, 'http://news.ycombinator.com')
c.perform()

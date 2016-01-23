#coding: utf-8

import urllib2

res = urllib2.urlopen("http://daily.2ch.net/newsplus/subback.html")
buf = res.read()
utf = buf.decode('utf-8')
print utf

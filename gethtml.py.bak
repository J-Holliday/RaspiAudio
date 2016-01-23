#!/usr/bin/env python
#coding: utf-8

import urllib2
import re
import socket
import htmlentitydefs

class news:
  @classmethod
  def unescape_html_entity(self,text):
    reference_regex = re.compile(u'&(#x?[0-9a-f]+|[a-z]+);', re.IGNORECASE)
    num16_regex = re.compile(u'#x\d+', re.IGNORECASE)
    num10_regex = re.compile(u'#\d+', re.IGNORECASE)

    result = ''
    i = 0
    while True:
        match = reference_regex.search(text, i)
        if match is None:
            result += text[i:]
            break

        result += text[i:match.start()]
        i = match.end()
        name = match.group(1)

        if name in htmlentitydefs.name2codepoint.keys():
            result += unichr(htmlentitydefs.name2codepoint[name])
        elif num16_regex.match(name):
            result += unichr(int(u'0'+name[1:], 16))
        elif num10_regex.match(name):
            result += unichr(int(name[1:]))

    return result

  @classmethod
  def getNews(self,url):
    socket.setdefaulttimeout(10.0)
    # 正規表現のパターンを定義 - タグ消し
    remove_tag = re.compile(r'<.*?>')

    try:
        htmldata = urllib2.urlopen(url)
    except urllib2.HTTPError as err:
        print('HTTPError')
        print(err)
    except urllib2.URLError as err:
        print('URLError')
        print(err)
        if isinstance(err.reason, socket.timeout):
            print('timeout')
    else:
        # print('Get HTML')
        pass

    content = htmldata.read()
    htmldata.close()
    response = news.unescape_html_entity(content.decode('shift-jis')).encode('utf-8')
    f = open("news.txt","w")
    f.write(response)
    f.close()

  @classmethod
  def get(self):
    url = "http://daily.2ch.net/newsplus/subback.html"
    news.getNews(url)

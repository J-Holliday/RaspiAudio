# -*- coding: utf-8 -*-
from musicPlayer import musicPlayer
from newsStation import newsStation
from newsStation import newsparser
from yukkuri import yukkuri
import socket
import subprocess

def interpreter(order,msg): # orderは認識された音声 msgはそれ以外の引数
	#c = caster()
	if order == "再生":
		musicPlayer.audio.play()
	elif order == "停止" and musicPlayer.audio.flag == 1:
		musicPlayer.audio.stop()
	elif order == "選択":
		print 2
		musicPlayer.select.callSelectMode()
		print 3
	elif order == "ニュース":
		return "playnews"
	elif order == "停止" and speker.flag == 1:
		#speaker.stopnews()
		return "stopnews"
	#elif order == "話題":
		#c.newsByMain()
	elif musicPlayer.select.flag == 1:
		musicPlayer.select.selectMusic(order) 
	return "interpreter is correctly finished."

if __name__ == "__main__":
	host = 'localhost'
	port = 10500

	#news.get()
	newsparser.parser.parse("newsStation/news.txt")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	yukkuri.talk("ゆっくりしていってね")
	msg = ""
	newsflag = 0

	while True:
		res = s.recv(1024)
		if not res.find('WORD') == -1:	
			try:
				ary1 = res.split('WORD')
				ary2 = ary1[1].split('"')
				print ary2[1]
				msg = interpreter(ary2[1],msg)
			except:
				print("error in xml parser.")
		if msg == "playnews": newsflag += 1
		elif msg == "stopnews":
			newsflag = 0
			newsparser.speaker.stopnews()
		if newsflag > 0: newsparser.speaker.playnews()

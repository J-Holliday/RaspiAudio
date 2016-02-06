# -*- coding: utf-8 -*-
from musicPlayer import musicPlayer
from newsStation import newsparser
from yukkuri import yukkuri
from mail import mail
import socket
import subprocess

def interpreter(order,msg): # orderは認識された音声 msgはそれ以外の引数
	#c = caster()
	print("newsparser.speaker.flag :" + str(newsparser.speaker.flag))
	if order == "再生":
		musicPlayer.audio.play()
	elif order == "停止" and musicPlayer.audio.flag == 1:
		print("stop with audio.")
		musicPlayer.audio.stop()
	elif order == "選択":
		musicPlayer.select.callSelectMode()
	elif order == "ニュース":
		newsparser.speaker.playnews()
	elif order == "停止" and newsparser.speaker.flag == 1:
		print("stop with news.")
		newsparser.speaker.stopnews()
		#return "stopnews"
	#elif order == "話題":
		#c.newsByMain()
	elif musicPlayer.select.flag == 1:
		musicPlayer.select.selectMusic(order) 
	elif order == "Gmail":
		print "callgmail"
		hoge = mail.checkGmail()
		print hoge
		yukkuri.talk(hoge)
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

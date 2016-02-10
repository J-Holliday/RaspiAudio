# -*- coding: utf-8 -*-
from musicPlayer import musicPlayer
from newsStation import newsparser
from yukkuri import yukkuri
from mail import mail
from semanticAnalysis import semanticAnalysis as sa
import socket
import subprocess

def interpreter(order,msg): # orderは認識された音声 msgはそれ以外の引数
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
	elif musicPlayer.select.flag == 1:
		musicPlayer.select.selectMusic(order) 
	elif order == "Gmail":
		print "callgmail"
		hoge = mail.checkGmail()
		print hoge
		yukkuri.talk(hoge)

	return "interpreter is correctly finished."

def interpreter2(msg):
	"""msg is should be string-array type."""
	sa.send(msg)
	#for word in msg:
	#	print "製作中だよ"

if __name__ == "__main__":
	host = 'localhost'
	port = 10500

	#news.get()
	newsparser.parser.parse("newsStation/news.txt")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	yukkuri.talk("ゆっくりしていってね")
	msg = ""
	sentenceFlag = 0
	sentence = []

	while True:
		res = s.recv(1024)
		if not res.find('WORD') == -1:	
			try:
				ary1 = res.split('WORD')
				ary2 = ary1[1].split('"')
				print ary2[1]
				if ary2[1] == "<s>":
					sentenceFlag = 1
				elif ary2[1] == "</s>":
					sentenceFlag = 0
					print str(sentence).decode("unicode-escape")

				if sentenceFlag == 1 and not ary2[1] == "<s>":
					sentence.append(unicode(ary2[1],"utf-8","ignore"))

				if sentenceFlag == 0:
					interpreter2(sentence)
					sentence = []
				#msg = interpreter(ary2[1],msg)
			except:
				print("error in xml parser.")

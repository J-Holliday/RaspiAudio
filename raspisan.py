# -*- coding: utf-8 -*-
from musicPlayer import musicPlayer
from newsStation import newsparser
from yukkuri import yukkuri
from mail import mail
from semanticAnalysis import semanticAnalysis as sa
import socket
import subprocess
import requests

def decoder(order):
	if order == 20:
		musicPlayer.audio.play()
	elif order == 23 and musicPlayer.audio.flag == 1:
		musicPlayer.audio.stop()
	#elif order == 24:
	#	musicPlayer.select.callSelectMode()
	elif order == 30:
		newsparser.speaker.playnews()
	elif order == 31 and newsparser.speaker.flag == 1:
		print("stop with news.")
		newsparser.speaker.stopnews()
	#elif musicPlayer.select.flag == 1:
	#	musicPlayer.select.selectMusic(order) 
	#elif order == "Gmail":
	#	print "callgmail"
	#	hoge = mail.checkGmail()
	#	print hoge
	#	yukkuri.talk(hoge)

	return "decoder is correctly finished."

if __name__ == "__main__":
	host = 'localhost'
	port = 10500

	#news.get()
	newsparser.parser.parse("newsStation/news.txt")
	yukkuri.talk("ゆっくりしていってね")
	msg = ""
	sentenceFlag = 0
	sentence = []
	url = "http://192.168.100.101:2222/asr_julius/"
	files = {
		"myFile": open("voice/record.wav", "rb")
	}
	s = requests.Session()
	while True:
		r = s.post(url, files=files)
		ary = r.text.split("\n")
		data = ary[0].split(":")
		words = data[1].strip(" ").split(" ")
		on = sa.send(words)
		print str(words).decode("unicode-escape")
		print "OrderNumber:%s" % str(on)
		quit()
		decoder(int(on))

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
					on = sa.send(sentence)
					print "OrderNumber:%s" % str(on)
					sentence = []
				#msg = interpreter(ary2[1],msg)
			except:
				print("error in xml parser.")

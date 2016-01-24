# -*- coding: utf-8 -*-
import socket
import subprocess
import audio
import select
import yukkuri

def newsByMain():
	u"""この関数はnewsparser.pyを補完します。
	将来的に、統合される予定です。
	"""
	print("ニュースを探しています")
	msg = speaker.randomselect()
	print msg
	msg2 = msg.replace("c2ch.net","").replace("2ch.net","")
	msg3 = msg2.replace(" ","")
	print msg3
	subprocess.Popen("/home/pi/workspace/raspi-audio/download/aquestalkpi/AquesTalkPi " + msg3 + " | aplay -q",shell=True)

def interpreter(order,msg): # orderは認識された音声 msgはそれ以外の引数
	a = audio()
	s = select()
	if order == "再生":
		a.play()
	elif order == "停止" and a.flag == 1:
		a.stop()
	elif order == "選択":
		s.callSelectMode()
	elif order == "ニュース":
		return "playnews"
	elif order == "停止" and speker.flag == 1:
		#speaker.stopnews()
		return "stopnews"
	elif order == "話題":
		newsByMain()
	elif s.flag == 1:
		s.selectMusic(order) 
	return "interpreter is correctly finished."

if __name__ == "__main__":
	host = 'localhost'
	port = 10500

	from gethtml import news
	from newsparser import parser
	from newsparser import speaker
	#news.get()
	parser.parse("news.txt")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	yukkuri("ゆっくりしていってね")
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
		if msg == "playnews":
			print("newsflag is incremented.")
			newsflag += 1
		elif msg == "stopnews":
			newsflag = 0
			print("newsflag is zero")
			speaker.stopnews()
		if newsflag > 0:
			print("call speaker.playnews()")
			speaker.playnews()

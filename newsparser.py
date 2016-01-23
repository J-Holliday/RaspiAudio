# -*- coding: utf-8 -*-
import random
import subprocess

class parser:
	@classmethod
	def parse(self,file):
		f = open(file,"r")
		res = f.read()
		f.close()
		ary = res.split("</a>")
		strout = ""
		n = 0
		for line in ary:
			if line.find("【") >= 0:
				ary2 = line.split(":")
				buf = ""
				if len(ary2) < 2:
					buf = ""
				else:
					buf = ary2[1]
				ary3 = buf.split("[")
				buf2 = ary3[0].split("(")
				strout += buf2[0].replace("c2ch.net","") + "\n"
				n += 1
		f = open("newsparsed.txt","w")
		f.write(strout)
		f.close()
		ftopic = open("newstopic.txt","w")
		ftopic.write(str(n))
		ftopic.close()
		print("parsing finish.")

class speaker:

	playProc = subprocess.Popen(["echo", "initialize speaker"])
	flag = 0	# for stop play-loop

	@classmethod
	def randomselect(self):
		print("randomselect is called.")
		ftopic = open("newstopic.txt","r")
		restopic = ftopic.read()
		ftopic.close()
		print("restopic is " + restopic)
		index = random.randint(1,int(restopic))
		n = 1
		print("random-index is" + str(index))
		f = open("newsparsed.txt","r")
		res = f.read()
		f.close()
		ary = res.split("\n")
		for line in ary:
			if n == index:
				return line
			else:
				n += 1
		return "None"

	@classmethod
	def playnews(self):
		if speaker.flag == 1:
			return
		print("speker.playnews is called.")
		if  speaker.playProc.poll() == 0:
			msg = speaker.randomselect()
			print msg
			msg2 = msg.replace("c2ch.net","").replace('2ch.net','')
			msg3 = msg2.replace(" ","")
			print msg3
			speaker.playProc = subprocess.Popen("/home/pi/workspace/raspi-audio/download/aquestalkpi/AquesTalkPi " + msg3 + " | aplay -q",shell=True)
			speaker.flag == 1
		else:
			print("news process is executed.")
			print(str(speaker.playProc.poll()))

	@classmethod
	def stopnews(self):
		print("speaker.stopnews is called.")
		speaker.playProc.terminate()
		spekaker.flag == 0

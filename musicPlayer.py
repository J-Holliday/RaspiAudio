import subprocess

class audio:
	
	playProc = subprocess.Popen(["echo","initialize audio"])
	flag = 0

	def play(self):
		if audio.flag == 1:
			return
		print("audio.play is called")
		f = open("selectBuffer","r")
		aroot = "/home/pi/workspace/raspi-audio/raspisan/music/"
		afile = aroot + f.read()
		print(afile)
		if afile[-3:] == "mp3":
			audio.playProc = subprocess.Popen(["mpg321",afile])
		elif afile[-3:] == "wav":
			audio.playProc = subprocess.Popen(["aplay",afile])
		audio.flag = 1

	def stop(self):
		print("audio.stop is called")
		audio.playProc.terminate()
		audio.flag = 0
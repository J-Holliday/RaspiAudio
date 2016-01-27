import subprocess

class yukkuri:

    aquestalk = "/home/pi/workspace/raspi-audio/downloads/aquestalkpi/AquesTalkPi"

    @classmethod
    def talk(self,msg):
        yukkuri.proc = subprocess.call(yukkuri.aquestalk + " " + msg + " | aplay -q", shell=True)

    @classmethod
    def talkbg(self,msg):
        yukkuri.proc = subprocess.Popen(yukkuri.aquestalk + " " + msg + " | aplay -q", shell=True)

import subprocess

aquestalk = "/home/pi/workspace/raspi-audio/downloads/aquestalkpi/AquesTalkPi"

def talk(msg):
    subprocess.call(aquestalk + " " + msg + " | aplay -q", shell=True)

def talkbg(msg):
    subprocess.Popen(aquestalk + " " + msg + " | aplay -q", shell=True)

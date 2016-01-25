import subprocess

class audio:

  playProc = subprocess.Popen(["echo","initialize audio"])
  flag = 0

  def play(self):
    if audio.flag == 1:
      return
    print("audio.play is called")
    f = open("musicPlayer/selectBuffer.txt","r")
    aroot = "/home/pi/workspace/raspi-audio/RaspiAudio/music/"
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

class select:

  flag = 0 # not select mode
  master = [""]

  def __init__(self):
    print("select init calling")
    select.master = self.readMaster()
    print("select init finish")

  def callSelectMode(self):
    print 10
    self.yukkuri("音楽を選んでください")
    print 11
    select.flag = 1

  def selectMusic(self,key):
    if key.find("KEY") == -1:
      return
    res = self.searchMusic(key)
    if res[0] == "None Array":
      return
    self.yukkuri(res[6] + "を選択しました")
    path = res[1] + "/" + res[2] + "/" + res[3] + res[4]
    f = open("musicPlayer/selectBuffer.txt","w")
    f.write(path)
    f.close()
    select.flag = 0

  def readMaster(self):
    print("readmaster is called.")
    f = open("musicPlayer/musicMaster.csv","r")
    str = f.read()
    f.close()
    ary = str.split('\n')
    return ary

  def searchMusic(self,key):
    print("start searchMusic")
    for line in select.master:
        if line.find(key) >= 0:
          ary = line.split(',')
          print("music is found.")
          return ary
        else:
          print(line)
    ary = ["None Array"]
    print("music is not found.")
    return ary
  
  def yukkuri(self,str):
    subprocess.check_output("/home/pi/workspace/raspi-audio/download/aquestalkpi/AquesTalkPi " + str + " | aplay -q",shell=True)
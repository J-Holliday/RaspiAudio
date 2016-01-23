import subprocess

class audio:

  aroot = "/home/pi/workspace/raspi-audio/raspisan/music/"
  flag = 0
  playProc = subprocess.Popen(["echo","initialize audio"])

  @classmethod
  def play(self):
    if audio.flag == 1:
        return
    f = open("selectBuffer","r")
    afile = audio.aroot + f.read()
    f.close()
    res = audio.callProc(afile)
    audio.flag = 1
    return res
    
  @classmethod
  def callProc(self,afile):
    ary = afile.split(".")
    ext = ary[len(ary) - 1]
    if ext == "mp3":
        audio.playProc = subprocess.Popen(["mpg321",afile])
        return 0
    elif ext == "wav":
        audio.playProc = subprocess.Popen(["aplay",afile])
        return 0
    else:
    	return 1 # unsupported audio file

  @classmethod
  def stop(self):
    audio.playProc.terminate()
    audio.flag = 0
    return 0
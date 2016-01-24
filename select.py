import yukkuri

class select:

  flag = 0 # not select mode
  master = [""]

  def __init__(self):
    """If I want to add music by User-Mode,
    musicMaster.csv is updated.
    Therefore, calling readMaster is treated as instance method."""
    select.master = self.readMaster()

  def callSelectMode(self):
    yukkuri.speak("‰¹Šy‚ğ‘I‚ñ‚Å‚­‚¾‚³‚¢")
    select.flag = 1

  def selectMusic(self,key):
    if key.find("KEY") == -1:
      return
    res = self.searchMusic(key)
    if res[0] == "None Array":
      return
    yukkuri.speak(res[6] + "‚ğ‘I‘ğ‚µ‚Ü‚µ‚½")
    path = res[1] + "/" + res[2] + "/" + res[3] + res[4]
    f = open("selectBuffer","w")
    f.write(path)
    f.close()
    select.flag = 0

  def readMaster(self):
    f = open("musicMaster.csv","r")
    str = f.read()
    f.close()
    ary = str.split('\n')
    return ary

  def searchMusic(self,key):
    for line in select.master:
      if line.find(key) >= 0:
        ary = line.split(',')
        return ary
    ary = ["None Array"]
    return ary
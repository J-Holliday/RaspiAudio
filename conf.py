class path:
  FILE_ROOT = "conf/root.conf"
  FILE_DOWNLOADS = "conf/downloads.conf"
  root = ""
  aroot = "" 		# audiofile "music"
  downloads = ""
  
  
  def __init__(self):
    path.root = path.getRoot()
    path.aroot = path.root + "music/"
    path.downloads = path.getDownloads()
  
  def getRoot(self):
    f = open(FILE_ROOT,"r")
    res = f.read()
    f.close()
    return res
  
  def getDownloads(self):
    f = open(FILE_DOWNLOADS,"r")
    res = f.read()
    f.close()
    return res
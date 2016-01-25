import subprocess
from newsparser import speaker

class caster:
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
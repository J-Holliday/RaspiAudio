import subprocess
from conf import path

class yukkuri
  @classmethod
  def speak(str):
    c = conf()
    command = c.downloads + "aquestalkpi/AquesTalkPi " + str + " | aplay -q"
    subprocess.check_output(command, shell=True)
  
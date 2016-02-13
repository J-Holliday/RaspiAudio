import subprocess
import time
import os

print os.getcwd()
gproc = subprocess.Popen("voice/rokuon.sh voice/record.wav 0", shell=True)
time.sleep(1.0)
print "gproc.pid:%s" % str(gproc.pid)
subprocess.call("ps -l", shell=True)
subprocess.call("kill " + str(gproc.pid+2), shell=True)
subprocess.call("ps -l", shell=True)

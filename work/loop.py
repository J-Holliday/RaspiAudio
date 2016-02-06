import subprocess

class process:
	proc = subprocess.Popen("echo init.",shell=True)
	
	def start(self):
		process.proc = subprocess.Popen(["python","while.py"])
		#process.proc = subprocess.Popen("aplay record.wav",shell=True)
		#process.proc = subprocess.Popen("python while.py",shell=True)
	
	def stop(self):
		process.proc.terminate()
		print("termination is executed.")
		p = subprocess.Popen("ps",shell=True)

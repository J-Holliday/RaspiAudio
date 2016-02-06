import threading

def hello():
		print("hello")
		t=threading.Timer(5,hello)
		t.start()
			
threads=[]
t=threading.Timer(5,hello)
t.start()	

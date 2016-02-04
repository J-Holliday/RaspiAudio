f = open("subject.csv")
sub = f.read()
f.close()
line = sub.split("\n")
item = list()
for i in range(1,len(line)-1):
	item.append(line[i].split(","))

def send(sentence):
	"""
	send() execute semantic-analysis.
	sentence is array of string.
	length is variable.
	"""
	searchSubject(sentence)

def searchSubject(sentence):
	for word in sentence:
		print 1
			

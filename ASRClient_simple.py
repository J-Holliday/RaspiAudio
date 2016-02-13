import requests
url = "http://192.168.100.101:2222/asr_julius/"
#url = "http://192.168.100.125:8000/asr_julius/"
#url = "http://10.0.2.15:8000/asr_julius/"
files = {
	'myFile': open('voice/record.wav', 'rb')
}
s = requests.Session()
r = s.post(url, files=files)
print r.text

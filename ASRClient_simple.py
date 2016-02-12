import requests
url = "http://10.0.2.15:8000/asr_julius/"
files = {
	'myFile': open('test_16000.wav', 'rb')
}
s = requests.Session()
r = s.post(url, files=files)
print r.text

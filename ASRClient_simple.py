import requests
url = "http://192.168.100.125:8080/asr_julius/"
files = {
	'myFile': open('test_16000.wav', 'rb')
}
s = requests.Session()
r = s.post(url, files=files)
print r.text

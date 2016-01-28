import socket

host = '127.0.0.1'
port = 10501

print 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 1
sock.bind((host, port))
print 2
sock.listen(1)
print 3
conn, address = sock.accept()
print 4
while True:
    msg = raw_input("-->")
    if msg == "exit": break
    conn.send('WORD"' + msg + '"')

conn.close()

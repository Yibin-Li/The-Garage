import socket
mysocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4inf.com', 80))
mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode())# encode() must be added in Python 3


while True:
    data = mysocket.recv(512).decode() # decode() must be added in Python 3
    if len(data)<1:
        break
    print (data)
# help(socket.socket.recv)

mysocket.close()


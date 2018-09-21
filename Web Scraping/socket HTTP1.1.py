
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET /code/intro-short.txt HTTP/1.1\n'.encode())
mysock.send('Host: www.pythonlearn.com\n\n'.encode())

while True:
    data = mysock.recv(512).decode()
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()

import socket;
import time;

HOST = '';
PORT = 21257;
BUFFERSIZE = 1024;
ADDR = (HOST, PORT);

tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcpServerSocket.bind(ADDR);
tcpServerSocket.listen(5);

while True:
	print('waiting for connection...');
	tcpCLientSocket, addr = tcpServerSocket.accept();
	print('...connection from :', addr);
	
	while True:
		data = tcpCLientSocket.recv(BUFFERSIZE);
		if not data:
			break;
		tcpCLientSocket.send(('[%s]%s'%(time.ctime(), data.decode('utf-8'))).encode('utf-8'));
	
	tcpCLientSocket.close();
tcpServerSocket.close();


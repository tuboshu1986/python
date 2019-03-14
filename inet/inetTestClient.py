import socket;

HOST = 'localhost';
PORT = 21257;
BUDDERSIZE = 1024;
ADDR = (HOST, PORT);

tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcpClientSocket.connect(ADDR);
while True:
	data = input(">>");
	if not data:
		break;
	tcpClientSocket.send(data.encode('utf-8'));
	data = tcpClientSocket.recv(BUDDERSIZE);
	if not data:
		break;
	print(data.decode('utf-8'));
tcpClientSocket.close();


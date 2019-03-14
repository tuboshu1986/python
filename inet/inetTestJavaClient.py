import socket;

HOST = 'localhost';
PORT = 9090;
BUDDERSIZE = 1024*10;
ADDR = (HOST, PORT);

tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcpClientSocket.connect(ADDR);

with open("D:/workspace/temp/kodi.txt", "rb") as f:
	while True:
		data = f.read(BUDDERSIZE);
		if(data):
			tcpClientSocket.send(data);
		else:
			break;

tcpClientSocket.close();


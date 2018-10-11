import socket;
import time;

HOST = "localhost";
PORT = 25051;
BUFSIZE = 1024;
ADDR = (HOST, PORT);

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
while True:
	data = input(">>>>");
	if not data:
		break;
	udpClient.sendto(data.encode(encoding="utf8"), ADDR);
	data, addr = udpClient.recvfrom(BUFSIZE);
	if not data:
		break;
	print(data.decode(encoding="utf8"));

udpClient.close();

import socket;
import time;

HOST = "";
PORT = 25051;
BUFSIZE = 1024;
ADDR = (HOST, PORT);

udpServerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udpServerSock.bind(ADDR);

while True:
	print("等待连接...");
	data, addr = udpServerSock.recvfrom(BUFSIZE);
	if not data:
		break;
	data = data.decode(encoding="utf8");
	print(data);
	udpServerSock.sendto(("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), data)).encode(encoding="utf8"), addr);
	
udpServerSock.close();


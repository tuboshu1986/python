# tcp socket

import socket;
import time;

HOST = "";
PORT = 25050;
BUFSIZE = 1024;
ADDR = (HOST, PORT);

tcpServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcpServerSock.bind(ADDR);
tcpServerSock.listen(5);

while True:
	print("等待连接...");
	tcpClientSock,ADDR = tcpServerSock.accept();
	print("已连接：" + str(tcpClientSock));
	print("已连接：" + str(ADDR));

	while True:
		data = tcpClientSock.recv(BUFSIZE).decode(encoding = "utf8");
		if not data:
			break;
		tcpClientSock.send(("[%s] %s" % (time.ctime(), data)).encode(encoding = "utf8"));
	tcpClientSock.close();
tcpServerSock.close();


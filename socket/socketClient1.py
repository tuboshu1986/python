import socket;

HOST = "localhost";
PORT = 25050;
BUFSIZE = 1024;
ADDR = (HOST, PORT);

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
cs.connect(ADDR);
while True:
	data = input(">>>>").encode(encoding = "utf8");
	if not data:
		break;
	cs.send(data);
	data = cs.recv(BUFSIZE).decode(encoding = "utf8");
	if not data:
		break;
	print(data);
	
cs.close();
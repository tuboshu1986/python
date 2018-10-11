import re;

urlsFile = open("D:/黄泊/study-workspace/python/regular-expression/urls.txt", encoding="utf8");
urls = [];
for line in urlsFile:
	line = line.strip();
	if line and not line.startswith("#") :
		urls.append(line);

p = r"\?(\S+.jpg)$|\?(\S+.png)$|/(\S+.jpg)$|/(\S+.png)$";
for url in urls:
	m = re.search(p, url);
	if m and m.group(1):
		print(m.group(1));
	elif m and m.group(2):
		print(m.group(2));
	elif m and m.group(3):
		print(m.group(3));
	elif m and m.group(4):
		print(m.group(4));
	


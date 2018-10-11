# coding=gbk
# D:\黄泊\study-workspace\python\file\tmp\a.txt
# D:/黄泊/study-workspace/python/file/tmp/a.txt
fp = input("file path:");

f = open(fp, encoding = "utf8");
pageCount = 1;
while(True):
	print("------------------------------------------" + str(pageCount));
	lineCount = 0;
	for i in range(5):
		line = f.readline();
		if not line:
			print("---------------------file end");
			break;
		print("---------------------line no : " + str(lineCount + 1));
		print(line);
		lineCount += 1;
	
	print("------------------------------------------" + str(pageCount) + " end");
	if lineCount < 4 :
		break;
	pageCount += 1;
	r = input("继续？(y/n):");
	if r=="n":
		break;

f.close();

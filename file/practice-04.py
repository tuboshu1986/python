# coding=gbk
# D:\�Ʋ�\study-workspace\python\file\tmp\a.txt
# D:/�Ʋ�/study-workspace/python/file/tmp/a.txt
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
	r = input("������(y/n):");
	if r=="n":
		break;

f.close();

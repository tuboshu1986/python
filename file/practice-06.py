# coding=gbk
# D:/黄泊/study-workspace/python/file/tmp/9-6-1.txt
# D:/黄泊/study-workspace/python/file/tmp/9-6-2.txt

def readLines(path):
	lines = [];
	f = None;
	try:
		f = open(path, encoding = "gbk");
		for line in f:
			lines.append(line);
	except (Exception) as e:
		print(e);
	finally:
		if f :
			f.close();
	return lines;
	
def splitChars(str):
	cs = [];
	for c in str:
		cs.append(c);
	return cs;

flines1 = readLines("D:/黄泊/study-workspace/python/file/tmp/9-6-1.txt");

flines2 = readLines("D:/黄泊/study-workspace/python/file/tmp/9-6-2.txt");

lineCount = len(flines1);
if lineCount < len(flines2):
	lineCount = len(flines2);

for lineIndex in range(lineCount):
	if flines1[lineIndex] != flines2[lineIndex]:
		cs1 = splitChars(flines1[lineIndex]);
		cs2 = splitChars(flines2[lineIndex]);
		
		for i,c in enumerate(cs1):
			if c != cs2[i]:
				print(str(lineIndex) + ":" + str(i));
				break;
		
		break;












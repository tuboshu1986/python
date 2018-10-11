import score;
import os;
import os.path;

scoreObj = score.Score();

"""
while True :
	s = int(input("输入："));
	if s == -1:
		break;

	msg = scoreObj.level1(s);
	print(msg);
	
print(scoreObj.scores);
print(scoreObj.scoreNames);
print(scoreObj.avg());

"""

# D:\黄泊\study-workspace\python\file\scores
p = input("dir : ");
for fname in os.listdir(p):
	if(os.path.isdir(p + os.sep + fname)):
		continue;
	f = open(p + os.sep + fname, "r");
	for line in f:
		try:
			print(scoreObj.level1(int(line.strip())));
		except:
			print("不是数字：" + line);
	f.close();

print(scoreObj.scores);
print(scoreObj.scoreNames);
print(scoreObj.avg());



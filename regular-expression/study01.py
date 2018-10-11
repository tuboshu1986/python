import re;

print("----------------------match");
	
m = re.match("asd|sad","sadasasd");
if m :
	print(m.group());
else:
	print(m);
	
print("----------------------match");
	
m = re.match("((\w\w\w)-(\d\d\d))","asd-123");
if m :
	print(m.group());
	print(m.group(1));
	print(m.group(2));
	print(m.group(3));
	print(m.groups());
else:
	print(m);
	
print("----------------------search");
	
m = re.search("asd|aaa","sadasasdaaaasdfbfdb");
if m :
	print(m.group());
else:
	print(m);
	
	
print("----------------------search");
	
#m = re.search(r"^aaa","aaa bbb ccc");
#m = re.search(r"\baaa","aaa bbb ccc");
m = re.search(r"\Bbbb","aaabbb ccc");
if m :
	print(m.group());
else:
	print(m);
	
	
print("----------------------findAll");
	
ms = re.findall("((asd)(aaa))","sadasasdaaaasdfbfdb");
for m in ms:
	print(m);


print("----------------------sub");
	
m = re.sub("X","xxx","aaaXbbbXccc");
print(m);

m = re.subn("X","xxx","aaaXbbbXccc");
print(m);



print("----------------------split");

m = re.split(",","aaa,bbb,ccc");
print(m);
m = re.split("[a-z]{3}","aaa-bbb-ccc".strip());
print(m);
m = re.split("\s\s|\t","aaa  bbb	ccc");
print(m);


print("----------------------贪心");

m = re.search("\w+?(a{0,1},)","aaa,bbb,ccc");
if m :
	print(m.group(1));












##csv处理
import csv;

filename = "C:/Users/dell/Desktop/话单/13877202362（网络） 4.csv";
filename1 = "C:/Users/dell/Desktop/aaa.csv";

arrData = [];

with open(filename, "r") as f:
	reader = csv.reader(f);
	for line in reader:
		arrData.append(line);
		print(line);
		
with open(filename1, "w") as f:
	writer = csv.writer(f);
	writer.writerows(arrData);
	
print("end");

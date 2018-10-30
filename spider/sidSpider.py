##获取sid

import requests_html;
import csv;

session = requests_html.HTMLSession();
r = session.get("http://www.bugujizhan.com/cdma.html");

table = r.html.find(".table-hover", first=True);
trs = table.find("tbody tr");

datas = [];
for tr in trs:
	trData = [];
	for td in tr.find("td"):
		trData.append(td.text.strip());
	datas.append(trData);
	
for idx in range(len(datas)):
	tr = datas[idx];
	if len(tr) > 0 and (not tr[0]) and idx > 0:
		tr[0] = datas[idx - 1][0];
	
with open("C:/Users/dell/Desktop/各市sid.csv", "w", newline='') as f:
	writer = csv.writer(f);
	for tr in datas:
		writer.writerow(tr);
		
		
print("end");
#https://timgsa.baidu.com/timgality=808c5a304.png
import re;

# http://tb.himg.baidu.com/sys/portrait/item/933679796779313931e432
# http://tb.himg.baidu.com/sys/portrait/item/ca1171e882a1e5b882e5b08fe799bd013b
# http://tb.himg.baidu.com/sys/portrait/item/08e1e88296e69d8ee9a39ee588803532316630
# url = "https://timgsa.baidu.com/timgality=808c5a304.png";
url = "https://timgsa.baidu.com/90.png";
p = r"\S{1,}/(\S+?.png)$";
m = re.search(p, url);
if m :
	print(m.group(1));


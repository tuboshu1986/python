import re;
import urllib.request;
import os;
import time;

class PageLoader():
	def __init__(self, url):
		self.url = url;
		self.html = None;
		self.imgUrls = [];
		
	def loadHtml(self):
		"业务方法：加载html"
		if self.html:
			return self.html;
		self.html = self.loadBytes(self.url).decode("utf-8", "ignore");
		return self.html;

	def saveImgs(self, basePath):
		"业务方法：保存图片"
		self.getImgUrls(self.html);
		nameIdx = 0;
		for imgUrl in self.imgUrls:
			f = None;
			try:
				f = open(basePath + os.sep + self.getPicNameFromUrl(imgUrl), "wb");
				f.write(self.loadBytes(imgUrl));
				f.flush();
				print(".");
				nameIdx += 1;
			except Exception as e:
				print(e);
			finally:
				if f :
					f.close();
	
	def getImgUrls(self, html):
		"工具方法：获取所有图片"
		if len(self.imgUrls) > 0 :
			return self.imgUrls;
		reg = r'src="([.*\S]*\.jpg)"';
		imgre = re.compile(reg);
		self.imgUrls = re.findall(imgre, html );
		return self.imgUrls;
		
	def loadBytes(self, url):
		"工具方法：获取页面二进制流"
		return urllib.request.urlopen(url).read();
	
	def getPicNameFromUrl(self, url):
		namePatterns = [r"\?(\S+?.jpg)$", r"\?(\S+?.png)$", r"\S{1,}/(\S+?.png)$", r"\S{1,}/(\S+?.png)$"];
		for p in namePatterns:
			m = re.search(p, url);
			if m :
				return m.group(1);
		return str(time.time()).replace(".", "") + ".jpg";
		
		
		
		
	
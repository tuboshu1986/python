## 文件对话框

import sys;
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication, QScrollArea);
from PyQt5.QtGui import (QPixmap);




class MyLabel(QLabel):
	def __init__(self, p):
		super().__init__(p);
		self.pixmap = None;
		
	def setPixmap(self, pixmap):
		super().setPixmap(pixmap);
		self.pixmap = pixmap;
		self.setScaledContents(True);
	
	def mouseDoubleClickEvent(self, e):
		size = self.parentWidget().size();
		#self.setPixmap(self.pixmap.scaledToHeight(size.height()));
		picSize = self.pixmap.size();
		self.resize(size.height()*(picSize.width()/picSize.height()), size.height());
		print(self.size());
		
		


class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		hbox = QHBoxLayout(self)
		pixmap = QPixmap("C:/Users/dell/Pictures/Saved Pictures/nature-river-stream-91505.jpg")
		#pixmap = pixmap.scaledToWidth(800);
		#pixmap = pixmap.scaledToHeight(800);
		
		label = MyLabel(self);
		label.setPixmap(pixmap);
		
		#label.
		
		self.scroll = QScrollArea();
		self.scroll.setWidget(label);
		
		hbox.addWidget(self.scroll);
		self.setLayout(hbox);
		
		self.show();
		
	def show(self):
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("简易");
		super().show();
		

if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());


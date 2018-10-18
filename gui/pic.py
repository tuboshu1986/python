## 文件对话框

import sys;
import re;
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QScrollArea, QFrame, QSplitter, QPushButton);
from PyQt5.QtGui import (QPixmap);
from PyQt5.QtCore import (Qt);



class MyLabel(QLabel):
	def __init__(self, p):
		super().__init__(p);
		self.pixmap = None;
		self.setStyleSheet("""
			QLabel{
				background-color:green;
			}
		""");
		
	def setPixmap(self, pixmap):
		super().setPixmap(pixmap);
		self.pixmap = pixmap;
		self.setScaledContents(True);
		self.fillShow();
	
	def mouseDoubleClickEvent(self, e):
		self.fillShow();
	
	def fillShow(self):
		size = self.parentWidget().size();
		#self.setPixmap(self.pixmap.scaledToHeight(size.height()));
		picSize = self.pixmap.size();
		if(size.width()/size.height() < picSize.width()/picSize.height()):
			self.resize(size.width(), size.width()*(picSize.height()/picSize.width()));
		else:
			self.resize(size.height()*(picSize.width()/picSize.height()), size.height());
		
		
class MyPicScroll(QScrollArea):
	def __init__(self, p):
		super().__init__();
		self.parent = p;
		self.setAlignment(Qt.AlignCenter);
		self.label = None;

	def setPic(self, path):
		if not self.label:
			self.label = MyLabel(self.parent);
		self.label.setPixmap(QPixmap(path));
		super().setWidget(self.label);
		
picArr = ["C:/Users/dell/Pictures/Saved Pictures/nature-river-stream-91505.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/17.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/2.gif",
	"C:/Users/dell/Pictures/Saved Pictures/4.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/18.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/6.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/15.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/19.jpg",
	"C:/Users/dell/Pictures/Saved Pictures/20.jpg"];
		
class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		left = QFrame(self);
		leftLayout = QVBoxLayout(left);
		left.setLayout(leftLayout);
		
		leftScroll = QScrollArea();
		leftScroll.setWidget(left);
		
		for p in picArr:
			m = re.search("/.+/(.+?\..+)$", p);
			if m:
				btn = QPushButton(m.group(1), left);
				btn.picPath = p;
				btn.clicked.connect(self.changePic);
				leftLayout.addWidget(btn);
				leftLayout.invalidate();
		
		right = QFrame(self);
		hbox = QHBoxLayout(right)
		right.setLayout(hbox);
	
		self.picPanel = right.picScroll = MyPicScroll(right);
		hbox.addWidget(right.picScroll);
		
		horiSplitter = QSplitter(Qt.Horizontal);
		horiSplitter.addWidget(leftScroll);
		horiSplitter.addWidget(right);
		horiSplitter.setStretchFactor(0, 2);
		horiSplitter.setStretchFactor(1, 8);
		
		boxLayout = QHBoxLayout(self);
		boxLayout.addWidget(horiSplitter);
		self.setLayout(boxLayout);
		
		self.show();
		
	def changePic(self, e):
		print(self.sender().picPath);
		self.picPanel.setPic(self.sender().picPath);
	
	def show(self):
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("简易");
		super().show();
		

if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());


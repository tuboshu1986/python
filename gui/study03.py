##布局
##绝对布局

import sys;
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication);

class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		lbl1 = QLabel("aaa", self);
		lbl1.move(50, 50);
		
		lbl2 = QLabel("bbb", self);
		lbl2.move(50, 100);
		
		lbl3 = QLabel("ccc", self);
		lbl3.move(100, 100);
		
		self.setGeometry(300, 300, 500, 400);
		self.setWindowTitle("绝对定位");
		self.show();
	

if __name__ == "__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());
		
		
	

	
	


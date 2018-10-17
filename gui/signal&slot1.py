# 事件和信号

import sys;

from PyQt5.QtCore import Qt;
from PyQt5.QtWidgets import (QMainWindow, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton, );

class Example(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();
	
	def initUI(self):
		btn1 = QPushButton("btn1", self);
		btn1.move(60, 50);
		btn1.clicked.connect(self.buttonClicked);

		btn2 = QPushButton("btn2", self);
		btn2.move(200, 50);
		btn2.clicked.connect(self.buttonClicked);
		
		btn3 = QPushButton("btn2", self);
		btn3.move(200, 100);
		btn3.clicked.connect(self.close);
		
		self.statusBar();
		
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("测试");
		self.show();
		
	def buttonClicked(self):
		sender = self.sender();
		print(sender);
		self.statusBar().showMessage(sender.text());
		
	def keyPressEvent(self, e):
		sender = self.sender();
		print(sender);
		if e.key() == Qt.Key_Escape:
			self.close();
		
		
if "__main__"==__name__:
	app = QApplication(sys.argv);
	a = Example();
	sys.exit(app.exec_());
	
		
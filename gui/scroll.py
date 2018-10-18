## 滚动条

import sys;
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QScrollArea, QFrame);

class Example(QWidget):
	
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		frame = QFrame(self);
		
		
		vbox = QVBoxLayout();
		for i in range(200):
			vbox.addWidget(QPushButton("OK"));
		
		vbox.addStretch(1);
		frame.setLayout(vbox);
		
		
		scroll = QScrollArea();
		scroll.resize(150, 400);
		scroll.setWidget(frame);
		
		vbox1 = QVBoxLayout();
		vbox1.addWidget(scroll);
		self.setLayout(vbox1);
		
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("bs");
		self.show();
	
	
if __name__ == "__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());

# 事件和信号

import sys;

from PyQt5.QtCore import (Qt, pyqtSignal, QObject);
from PyQt5.QtWidgets import (QMainWindow, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton, );

class Communicate(QObject):
	closeApp = pyqtSignal();

class Example(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();
	
	def initUI(self):
		self.c = Communicate();
		self.c.closeApp.connect(self.close);
		
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("测试");
		self.show();
		
	def mousePressEvent(self, e):
		self.c.closeApp.emit();
		
	def keyPressEvent(self, e):
		sender = self.sender();
		print(sender);
		if e.key() == Qt.Key_Escape:
			self.close();
		
	def close(self):
		sender = self.sender();
		print(sender);
	
if "__main__"==__name__:
	app = QApplication(sys.argv);
	a = Example();
	sys.exit(app.exec_());
	
		
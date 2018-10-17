# 事件和信号

import sys;

from PyQt5.QtCore import Qt;
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication);

class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
	
	def initUI(self):
		lcd = QLCDNumber(self);
		slider = QSlider(Qt.Horizontal, self);

		vbox = QVBoxLayout();
		vbox.addWidget(lcd);
		vbox.addWidget(slider);
		
		self.setLayout(vbox);
		slider.valueChanged.connect(lcd.display);
		
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("测试");
		self.show();
		
	def keyPressEvent(self, e):
		print(e.key());
		if e.key() == Qt.Key_Escape:
			self.close();
		
		
if "__main__"==__name__:
	app = QApplication(sys.argv);
	a = Example();
	sys.exit(app.exec_());
	
		
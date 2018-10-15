##布局
##绝对布局

import sys;
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication);

class Example(QWidget):
	
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		okButton = QPushButton("OK");
		cancelButton = QPushButton("Cancel");
		
		hbox = QHBoxLayout();
		hbox.addStretch(1);
		hbox.addWidget(okButton);
		hbox.addWidget(cancelButton);

		hbox1 = QHBoxLayout();
		hbox1.addStretch(1);
		hbox1.addWidget(QLabel("aaaa"));
		hbox1.addWidget(QLabel("bbbb"));
		hbox1.addStretch(1);

		vbox = QVBoxLayout();
		vbox.addStretch(1);
		vbox.addLayout(hbox);
		vbox.addLayout(hbox1);
		vbox.addStretch(1);
		
		self.setLayout(vbox);
		
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("bs");
		self.show();
	
	
if __name__ == "__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());
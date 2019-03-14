import sys;

from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QLabel, QLineEdit, QTextEdit;
from PyQt5.QtGui import QIcon,QFont;
from PyQt5.QtCore import QCoreApplication;

from ReStudyWidget import *;

class Example(ReStudyWidget):
	def __init__(self):
		super().__init__();
		self.initGridLayout1();
		
	def initAbsoluteUI(self):
		self.setToolTip("岁月的童话");
		
		exitBtn = QPushButton("退出", self);
		exitBtn.clicked.connect(QCoreApplication.instance().quit);
		exitBtn.resize(exitBtn.sizeHint());
		exitBtn.move(50, 50);
		
		exitLbl = QLabel("退出按钮", self);
		exitLbl.move(0, 50);
		
		super().initUI();
		
	def initBoxLayoutUI(self):
		exitBtn = QPushButton("退出", self);
		exitBtn.clicked.connect(QCoreApplication.instance().quit);
		exitBtn.resize(exitBtn.sizeHint());
		
		exitLbl = QLabel("退出按钮", self);
		
		hboxLaout = QHBoxLayout();
		hboxLaout.addStretch(1);
		hboxLaout.addWidget(exitLbl);
		hboxLaout.addWidget(exitBtn);
		
		vboxLayout = QVBoxLayout();
		vboxLayout.addStretch(1);
		vboxLayout.addLayout(hboxLaout);
		
		self.setLayout(vboxLayout);
		
		super().initUI();
		
	def initGridLayout(self):
		gridLayout = QGridLayout();
		self.setLayout(gridLayout);
		
		names = ['Cls', 'Bck', '', 'Close',
				'7', '8', '9', '/',
				'4', '5', '6', '*',
				'1', '2', '3', '-',
				'0', '.', '=', '+'];
		positions = [(i,j) for i in range(5) for j in range(4)];
		
		for (name, position) in zip(names, positions):
			if not name:
				continue;
			btn = QPushButton(name, self);
			gridLayout.addWidget(btn, *position);
				
		super().initUI();
		
	def initGridLayout1(self):
		gridLayout = QGridLayout();
		self.setLayout(gridLayout);

		gridLayout.setSpacing(5);#各单元格之间的间距
		
		gridLayout.addWidget(QLabel("title"), 1, 0);
		gridLayout.addWidget(QLineEdit(), 1, 1);
		
		gridLayout.addWidget(QLabel("author"), 2, 0);
		gridLayout.addWidget(QLineEdit(), 2, 1);
		
		gridLayout.addWidget(QLabel("content"), 3, 0);
		gridLayout.addWidget(QTextEdit(), 3, 1, 10, 1);
		
		super().initUI();
		
	def closeEvent(self, event):
		rely = QMessageBox.question(self, "Message", "确认关闭此窗口吗？", QMessageBox.Yes|QMessageBox.No, QMessageBox.No);
		if rely == QMessageBox.Yes:
			event.accept();
		else:
			event.ignore();

if __name__ == "__main__":
	app = QApplication(sys.argv);
	
	w = Example();
	
	sys.exit(app.exec_());

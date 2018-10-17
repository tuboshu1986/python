## 对话框

import sys;
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QColorDialog, QFrame, QLabel, QFontDialog, QApplication, QTextEdit, QMainWindow);
from PyQt5.QtGui import (QColor);

class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		self.btn = QPushButton("输入", self);
		self.btn.move(50, 30);
		self.btn.clicked.connect(self.showDialog);
		
		self.line = QLineEdit(self);
		self.line.move(130, 31);
		self.line.setReadOnly(True);

		##颜色框
		color = QColor(0, 0, 0);
		self.colorBtn = QPushButton("颜色", self);
		self.colorBtn.move(50, 70);
		self.colorBtn.clicked.connect(self.showColorDialog);
		
		self.frame = QFrame(self);
		self.frame.setStyleSheet("QWidget{background-color:%s}"%color.name());
		self.frame.setGeometry(130, 70, 150, 23);
		##颜色框
		
		##字体
		self.fontBtn = QPushButton("字体", self);
		self.fontBtn.move(50, 100);
		self.fontBtn.clicked.connect(self.showFontDialog);
		
		self.lbl = QLabel('Knowledge only matters', self)
		self.lbl.move(130, 100);
		self.lbl.resize(200,100);
		##字体
		
		self.show();
		
	def show(self):
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("简易");
		super().show();
		
	def showFontDialog(self):
		(font, ok) = QFontDialog.getFont();
		if ok:
			self.lbl.setFont(font);
	
	def showColorDialog(self):
		color = QColorDialog.getColor();
		if color.isValid():
			self.frame.setStyleSheet("QWidget{background-color:%s}"%color.name());
			#self.setStyleSheet("QWidget{background-color:%s}"%color.name());
		
	def showDialog(self):
		text,ok = QInputDialog.getText(self, "输入", "输入我的名字：");
		if(ok):
			self.line.setText(text);


if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());


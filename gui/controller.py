## 控件
import sys;
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication, QPushButton, QHBoxLayout, QFrame, QSplitter);
from PyQt5.QtCore import Qt;

class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		topLeft = QFrame(self);
		topLeft.setFrameShape(QFrame.StyledPanel);
		
		topRight = QFrame(self);
		topRight.setFrameShape(QFrame.StyledPanel);
		
		bottom = QFrame(self);
		bottom.setFrameShape(QFrame.StyledPanel);
		
		horizontalSplitter = QSplitter(Qt.Horizontal);
		horizontalSplitter.addWidget(topLeft);
		horizontalSplitter.addWidget(topRight);
		
		horizontalSplitter.resize(100, 100);
		
		verticalSplitter = QSplitter(Qt.Vertical);
		verticalSplitter.addWidget(horizontalSplitter);
		verticalSplitter.addWidget(bottom);
		
		boxLayout = QHBoxLayout(self);
		boxLayout.addWidget(verticalSplitter);
	
		self.setLayout(boxLayout);
	
		ck = QCheckBox("修改名称", bottom);
		ck.move(20, 20);
		ck.toggle();
		ck.stateChanged.connect(self.changeTitle);
		
		btn = QPushButton("选择", topLeft);
		btn.setCheckable(True);
		btn.move(20, 60);
		btn.clicked[bool].connect(self.changeColor);
		
		self.show();
		
	def changeColor(self, pressed):
		print(pressed);
		print(self.sender().isChecked());
		
	def changeTitle(self, state):
		print(state);
		if state == Qt.Checked:
			self.setWindowTitle("小明");
		else:
			self.setWindowTitle("小红");
		
	def show(self):
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("简易");
		super().show();
		
	

if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());






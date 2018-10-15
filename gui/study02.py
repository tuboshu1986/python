import sys;
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QToolTip, QPushButton, QMessageBox);
from PyQt5.QtGui import (QIcon, QFont);
from PyQt5.QtCore import QCoreApplication;

class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		QToolTip.setFont(QFont("SansSerif", 8));
		
		self.setToolTip("这是一个QWidget");
	
		btn = QPushButton("按钮", self);
		btn.setToolTip("这是<strong>按钮</strong>");
		btn.resize(60, 30);
		btn.move(50, 50);
		
		qbtn = QPushButton("关闭", self);
		qbtn.clicked.connect(QCoreApplication.instance().quit);
		qbtn.resize(qbtn.sizeHint());
		qbtn.move(50, 150);
	
		self.setGeometry(300,300,500,300);
		self.setWindowTitle("煎蛋");
		self.setWindowIcon(QIcon("qwe.png"));
		
		#self.center();
		self.show();
		
	def center(self):
		frame = self.frameGeometry();
		centerPoint = QDesktopWidget().availableGeometry().center();
		frame.moveCenter(centerPoint);
		self.move(frame.topLeft());
		
	def closeEvent(self, event):
		reply = QMessageBox.question(self, "消息", "你想退出吗？", QMessageBox.Yes|QMessageBox.No, QMessageBox.No);
		if reply == QMessageBox.Yes:
			event.accept();
		else:
			event.ignore();

if __name__ == "__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());


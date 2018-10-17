## 文件对话框

import sys;
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QColorDialog, QFrame, QLabel, QFontDialog, QApplication, QTextEdit, QMainWindow, QAction, QFileDialog);
from PyQt5.QtGui import (QColor,QIcon);

class Example(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		
		##文件目录
		self.textEdit = QTextEdit();
		self.setCentralWidget(self.textEdit);
		
		self.statusBar();
		
		self.fileAction = QAction(QIcon("1.jpg"), "打开", self);
		self.fileAction.setShortcut("ctrl+o");
		self.fileAction.setStatusTip("打开文件");
		self.fileAction.triggered.connect(self.showFileDialog);
		
		menubar = self.menuBar();
		fileMenu = menubar.addMenu("文件");
		fileMenu.addAction(self.fileAction);
		
		open = QAction();
		
		##文件目录
		
		
		self.show();
		
	def show(self):
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("简易");
		super().show();
		
	def showFileDialog(self):
		fname = QFileDialog.getOpenFileName(self, "打开文件", "/home");
		if fname[0]:
			print(fname);
			f = open(fname[0], encoding="utf8")
			with f:
				self.textEdit.setText(f.read());
	

if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());


import sys;

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication;
from PyQt5.QtGui import QIcon,QFont;
from PyQt5.QtCore import QCoreApplication;

from ReStudyWidget import *;

class Example(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		text = QTextEdit();
		self.setCentralWidget(text);
		
		exitAction = QAction(QIcon("icon.png"), "exit", self);
		exitAction.setStatusTip("退出");
		exitAction.triggered.connect(self.close);
		
		menuBar = self.menuBar();
		fileMenu = menuBar.addMenu("&File");
		fileMenu.addAction(exitAction);
		
		exitToolBar = self.addToolBar("&退出");
		exitToolBar.addAction(exitAction);
		
		self.statusBar();#创建状态栏
		
		self.show();
		
if __name__ == "__main__":
	app = QApplication(sys.argv);
	
	w = Example();
	
	sys.exit(app.exec_());

##	状态栏
##  菜单栏

import sys;
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, qApp, QToolBar);
from PyQt5.QtGui import QIcon;
from PyQt5.QtCore import QSize;

class Example(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		icon = QIcon("bitbug_favicon.ico");
		exitAction = QAction(icon, "Exit", self);
		exitAction.setShortcut("Ctrl+Q");
		exitAction.setStatusTip("退出");
		exitAction.triggered.connect(qApp.quit);
		
		self.statusBar().showMessage("Ready");
		
		menuBar = self.menuBar();
		fileMenu = menuBar.addMenu("&File");
		fileMenu.addAction(exitAction);
		
		menuBar.addMenu("&Edit");
		
		menuBar.addMenu("&Search");
		
		menuBar.addMenu("&View");
		
		toolBar = QToolBar("E");
		self.addToolBar(toolBar);
		toolBar.addAction(exitAction);
		toolBar.setIconSize(QSize(40, 40));
		
		self.setGeometry(300, 300, 500, 300);
		self.setWindowTitle("俄式");
		
		self.show();
		
if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());
	
	
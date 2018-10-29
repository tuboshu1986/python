## 文件对话框

import sys;
import re;
import os;
from PyQt5.QtWidgets import (QInputDialog, QMessageBox, QFileDialog, QAction, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QScrollArea, QFrame, QSplitter, QPushButton, QListWidget, QListWidgetItem, QMainWindow);
from PyQt5.QtGui import (QPixmap, QIcon);
from PyQt5.QtCore import (Qt);



class MyLabel(QLabel):
	def __init__(self, p):
		super().__init__(p);
		self.pixmap = None;
		self.setStyleSheet("""
			QLabel{
				background-color:green;
			}
		""");
		
	def setPixmap(self, pixmap):
		super().setPixmap(pixmap);
		self.pixmap = pixmap;
		self.setScaledContents(True);
		self.fillShow();
	
	def mouseDoubleClickEvent(self, e):
		self.fillShow();
	
	def fillShow(self):
		size = self.parentWidget().size();
		#self.setPixmap(self.pixmap.scaledToHeight(size.height()));
		picSize = self.pixmap.size();
		if(size.width()/size.height() < picSize.width()/picSize.height()):
			self.resize(size.width(), size.width()*(picSize.height()/picSize.width()));
		else:
			self.resize(size.height()*(picSize.width()/picSize.height()), size.height());
		
		
class MyPicScroll(QScrollArea):
	def __init__(self, p):
		super().__init__();
		self.parent = p;
		self.setAlignment(Qt.AlignCenter);
		self.label = None;

	def setPic(self, path):
		if not self.label:
			self.label = MyLabel(self.parent);
		self.label.setPixmap(QPixmap(path));
		super().setWidget(self.label);
		
class Example(QMainWindow):
	def __init__(self):
		super().__init__();
		self.currentPicList = None;
		self.currentPic = None;
		self.currentDic = None;
		self.initUI();

	def initUI(self):
		self.initPicPanel();
		self.initMenu();
		self.show();
		
		#self.setPicList(picArr);
		
	def initPicPanel(self):
		left = QFrame(self);
		leftLayout = QVBoxLayout(left);
		left.setLayout(leftLayout);
		
		self.picList = QListWidget(self);
		self.picList.itemClicked.connect(self.changePic);
		
		#leftScroll = QScrollArea();
		#leftScroll.setWidget(selfPicList);
		
		right = QFrame(self);
		hbox = QHBoxLayout(right)
		right.setLayout(hbox);
	
		self.picPanel = right.picScroll = MyPicScroll(right);
		hbox.addWidget(right.picScroll);
		
		horiSplitter = QSplitter(Qt.Horizontal);
		horiSplitter.addWidget(self.picList);
		horiSplitter.addWidget(right);
		horiSplitter.setStretchFactor(0, 1);
		horiSplitter.setStretchFactor(1, 6);
		self.setCentralWidget(horiSplitter);
		
		
	def initMenu(self):
		self.statusBar().showMessage("ready");
		menuBar = menubar = self.menuBar();
		toolBar = self.addToolBar("file");
		fileMenu = menuBar.addMenu("文件");
		
		dicAction = self.defindeAction('打开文件夹', 'Ctrl+O', '选择文件夹以显示其中的图片', self.openDicSelector);
		fileMenu.addAction(dicAction);
		toolBar.addAction(dicAction);
		
		goodDicAction = self.defindeAction('好的文件夹', 'Ctrl+G', '标记为有价值的文件夹', self.isGoodDic);
		fileMenu.addAction(goodDicAction);
		toolBar.addAction(goodDicAction);

		nextDicAction = self.defindeAction('下一个文件夹', 'Ctrl+D', '加载下一个文件夹', self.showNextPic);
		fileMenu.addAction(nextDicAction);
		toolBar.addAction(nextDicAction);
		
		lastDicAction = self.defindeAction('上一个文件夹', 'Ctrl+F', '加载上一个文件夹', self.showNextPic);
		fileMenu.addAction(lastDicAction);
		toolBar.addAction(lastDicAction);
		
		nexPicAction = self.defindeAction('下一张图片', 'Ctrl+N', '显示同目录的下一张图片', self.showNextPic);
		fileMenu.addAction(nexPicAction);
		toolBar.addAction(nexPicAction);
		
		lastPicAction = self.defindeAction('上一张图片', 'Ctrl+L', '显示同目录的上一张图片', self.showNextPic);
		fileMenu.addAction(lastPicAction);
		toolBar.addAction(lastPicAction);
		
	def defindeAction(self, title, shortcut, statusTip, actionFun):
		action = QAction(title, self)        
		action.setShortcut(shortcut);
		action.setStatusTip(statusTip);
		action.triggered.connect(actionFun);
		return action;
		
	def isGoodDic(self):
		if not self.currentDic:
			reply = QMessageBox.warning(self,"消息","未选中文件夹",QMessageBox.Yes);
			return;
		(text, ok) = QInputDialog.getText(self,'标记','标记文本:');
		if ok and text:
			with open(self.currentDic + os.sep + "m.log", "a") as mfile:
				mfile.write(text + "\n");
		
	def showNextPic(self):
		print(124);
		
	def showLastPic(self):
		print(124);
		
	def openDicSelector(self):
		try:
			pdic = "/home";
			if self.currentDic:
				pdic = os.path.dirname(self.currentDic);
			fname = QFileDialog.getExistingDirectory(self, '打开文件夹', pdic);
			if fname:
				ps = self.getPicsForDic(fname);
				if len(ps)==0:
					return;
				self.picList.clear();
				self.setPicList(ps);
				self.picPanel.setPic(ps[0][0]);
				self.currentDic = fname;
		except Exception as e:
			print(e);
		
	def getPicsForDic(self, path):
		fs = os.listdir(path);
		ps = [];
		if fs and len(fs)>0:
			for fn in fs:
				ps.append((path + os.sep + fn, fn));
		return ps;
		
	def setPicList(self, picArr):
		for p in picArr:
			if p:
				item = QListWidgetItem(p[1]);
				item.picPath = p[0];
				#item.setIcon(QIcon(p));
				self.picList.addItem(item);
		
	def changePic(self, e):
		try:
			print(e.picPath);
			self.picPanel.setPic(e.picPath);
		except Exception as e:
			print(e);
	
	def show(self):
		self.setGeometry(300, 200, 1200, 700);
		self.setWindowTitle("简易");
		super().show();
		

if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());


import os;
import traceback;
import shutil;
from PyQt5.QtWidgets import (QInputDialog, QMessageBox);
from PyQt5.QtWidgets import *;
from PyQt5.QtQuick import *;

print(">>>>文件工具包加载成功");

class PicFileUtil():
	
	deletedDir = "D:/hhh/f/";
	
	def __init__(self, p, basePath):
		super().__init__();
		if (not basePath or basePath == "") :
			QMessageBox.warning(self.pic, "消息", "必须选中一个目录", QMessageBox.Yes);
			return;
		self.pic = p;
		self.pathConfigStr = "-1,-1,0,1";
		self.pathConfig = None
		self.currentDir = None;
		self.currentDirIndex = None;
		self.basePath = basePath;
		print(">>>>" + basePath);
		self.dirs = None;
		self.analyzePathConfig();
		self.dirShower = None;


	def inputParentLevel(self, basePath):
		baseVal = "";
		if self.pathConfigStr:
			baseVal = self.pathConfigStr;
		(text, ok) = QInputDialog.getText(self.pic,'深度','输入配置信息:',text = baseVal);
		if not ok:
			QMessageBox.warning(self.pic, "消息", "必须输入内容", QMessageBox.Yes);
			return;
		self.pathConfigStr = text;
		self.analyzePathConfig();
		return self.pathConfigStr;
		
		
	def analyzePathConfig(self):
		pathConfigStr = self.pathConfigStr;
		subStrs = pathConfigStr.split(",");
		numbers = [];
		zeroIndex = -1;
		for index in range(len(subStrs)):
			subStr = subStrs[index];
			print(subStr);
			if (not self.isInt(subStr)):
				QMessageBox.warning(self.pic, "消息", "不是合法的配置信息", QMessageBox.Yes);
				return;
			subCfg = int(subStr);
			if (zeroIndex == -1 and subCfg == 0) :
				numbers.append(subCfg);
				zeroIndex = index;
				continue;
			if(zeroIndex == -1 and subCfg > 0):
				QMessageBox.warning(self.pic, "消息", "不是合法的配置信息", QMessageBox.Yes);
				return;
			if(zeroIndex > -1 and subCfg <= 0):
				QMessageBox.warning(self.pic, "消息", "不是合法的配置信息", QMessageBox.Yes);
				return;
			numbers.append(subCfg);
			
		self.pathConfig = numbers;
	
	
	def lastDir(self):
		self.dicList();
		dirIndex = self.currentDirIndex;
		if(dirIndex > 0):
			dirIndex = dirIndex - 1;
		tmpDir = self.dirs[dirIndex];
		self.currentDirIndex = dirIndex;
		self.currentDir = tmpDir;
		return self.subDir();
	
	
	def nextDir(self):
		self.dicList();
		dirIndex = self.currentDirIndex;
		if(dirIndex < (len(self.dirs) - 1)):
			dirIndex = dirIndex + 1;
		tmpDir = self.dirs[dirIndex];
		self.currentDirIndex = dirIndex;
		self.currentDir = tmpDir;
		return self.subDir();
		
	def refresh(self):
		if self.currentDir :
			self.dicList();
			return self.subDir();
		return None;
	
	def subDir(self):
		currentDir = self.currentDir;
		childDirs = None;
		childDir = currentDir;
		try:
			for index in range(len(self.pathConfig)):
				subCfg = self.pathConfig[index];
				if(subCfg > 0):
					childDirs = os.listdir(childDir);
					if childDirs and len(childDirs) >= subCfg:
						childDir = childDir + os.sep + childDirs[subCfg - 1];
					else:
						break;
		except Exception as e:
			traceback.print_exc()
		return childDir;
	
	
	def dicList(self):
		if self.dirs:
			return;
		basePath = self.basePath; 
		tmpPath = basePath;
		tmpDirName = None;
		for index in range(len(self.pathConfig)):
			subCfg = self.pathConfig[index];
			if subCfg<0 :
				print(subCfg);
				tmpDirName = os.path.basename(tmpPath);
				tmpPath = os.path.dirname(tmpPath);
		print(tmpPath);
		self.dirs = os.listdir(tmpPath);
		self.currentDir = tmpDirName;
		for index in range(len(self.dirs)):
			self.dirs[index] = tmpPath + os.sep + self.dirs[index];
			if(os.path.basename(self.dirs[index]) == tmpDirName):
				self.currentDirIndex = index;
		
	
	def isInt(self, str):
		try:
			num = int(str);
			return isinstance(num, int)
		except Exception as e:
			print(">>>>不是数字");
		return False;
		
		
	def showDirList(self):
		self.dirShower = DirPanel(self.pic);
		dirList = QListWidget(self.dirShower);
		dirList.setStyleSheet("""
			QLabel{
				background-color:red;
			}
		""");
		for index in range(len(self.dirs)):
			item = QListWidgetItem(os.path.basename(self.dirs[index]));
			item.dirIndex = index;
			dirList.addItem(item);
		dirList.setCurrentRow(self.currentDirIndex);
		dirList.itemDoubleClicked.connect(self.selectDir);
		
		vbox  = QVBoxLayout();
		vbox.addWidget(dirList);
		
		self.dirShower.setLayout(vbox);
		self.dirShower.setWindowTitle("同级目录");
		self.dirShower.setGeometry(500, 100, 600, 800);
		self.dirShower.show();
		

	def selectDir(self, item):
		print(self.dirs[item.dirIndex]);
		self.currentDirIndex = item.dirIndex;
		self.currentDir = self.dirs[item.dirIndex];
		self.dirShower.close();
		self.pic.refresh();
		
		
	def deleteCurrentDir(self):
		cDir = self.dirs.pop(self.currentDirIndex);
		if(self.currentDirIndex >= len(self.dirs)):
			self.currentDirIndex = len(self.dirs) - 1;
		self.currentDir = self.dirs[self.currentDirIndex];
		self.pic.refresh();
		self.moveDir(cDir);
		return cDir;
		
		
	def moveDir(self, srcDir):
		shutil.move(srcDir, self.deletedDir);
		
		
class DirPanel(QWidget):
	def __init__(self, p):
		super().__init__();
		self.parent = p;
	
	
	def hideEvent(self, v):
		self.parent.show();
		
		
	def showEvent(self, v):
		self.parent.hide();
		
		
		
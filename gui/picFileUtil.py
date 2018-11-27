import os;
import traceback;
from PyQt5.QtWidgets import (QInputDialog, QMessageBox);

print(">>>>文件工具包加载成功");

class PicFileUtil():
	
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
		
		
		
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow;
from PyQt5.QtGui import QIcon;

class ReStudyWidget(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		self.resize(500, 300);
		self.move(300, 300);
		self.setWindowTitle("重来");
		self.setWindowIcon(QIcon("icon.png"));
		self.center();
		self.show();
		
	def center(self):
		frameGeometry = self.frameGeometry();
		centerPointer = QDesktopWidget().availableGeometry().center();
		print(centerPointer);
		frameGeometry.moveCenter(centerPointer);
		print(frameGeometry.topLeft());
		self.move(frameGeometry.topLeft());
	
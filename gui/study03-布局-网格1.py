##布局
##绝对布局

import sys;
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QApplication);

class Example(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
		
	def initUI(self):
		grid = QGridLayout();
		self.setLayout(grid);
		
		title = QLabel("标题");
		author = QLabel("作者");
		review = QLabel("内容");
		
		titleEdit = QLineEdit();
		authorEdit = QLineEdit();
		reviewEdit = QTextEdit();
		
		grid.addWidget(title, 1, 0);
		grid.addWidget(titleEdit, 1, 1);
		
		grid.addWidget(author, 2, 0);
		grid.addWidget(authorEdit, 2, 1);
		
		grid.addWidget(review, 3, 0);
		grid.addWidget(reviewEdit, 3, 1, 5, 1);
		
		self.move(300,300);
		self.setWindowTitle("cascas");
		self.show();
		

if __name__=="__main__":
	app = QApplication(sys.argv);
	e = Example();
	sys.exit(app.exec_());




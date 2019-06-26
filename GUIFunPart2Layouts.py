import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
	numClicks = 0
	
	def __init__(self):
		super().__init__()
		
		self.init_ui()
		
	def init_ui(self):
		
		self.b = QtWidgets.QPushButton('Push Me')
		self.l = QtWidgets.QLabel('Number of Clicks: ' + str(self.numClicks))
		
		h_box = QtWidgets.QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.l)
		h_box.addStretch()
		
		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.b)
		v_box.addLayout(h_box)
		
		self.setLayout(v_box)
		self.setWindowTitle('PyQt5 Lesson 5')
		
		self.b.clicked.connect(self.btn_click)
		
		self.show()
	
	def btn_click(self):
		self.numClicks += 1
		self.l.setText('Number of Clicks: ' + str(self.numClicks))



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)

class Window(QWidget):
	def __init__(self):
		super().__init__()
		
		self.init_ui()
		
	def init_ui(self):
		self.lbl = QLabel('Which do you like best?')
		self.dog = QRadioButton('Dogs')
		self.cat = QRadioButton('Cats')
		self.btn = QPushButton('Submit')
		
		layout = QVBoxLayout()
		layout.addWidget(self.lbl)
		layout.addWidget(self.dog)
		layout.addWidget(self.cat)
		layout.addWidget(self.btn)
		
		self.setLayout(layout)
		self.setWindowTitle('PyQt5 Lesson 10')
		
		#rather than connect, you can use self.dog.toggled (meaning one of the radiobuttons) 
		#and that will call the function right as the radiobutton is clicked rather than
		#another button
		self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.lbl))
		self.show()

	def btn_clk(self, chk, lbl):
		if chk:
			lbl.setText('You Like Dogs!')
		else:
			lbl.setText('You Like Cats!')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
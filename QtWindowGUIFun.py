import sys
from PyQt5 import QtWidgets,QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	
	#l1 = QtWidgets.QLabel(w)
	#l2 = QtWidgets.QLabel(w)
	#l1.setText('Hello World')
	#l2.setPixmap(QtGui.QPixmap('Figure_1.png'))
	
	b = QtWidgets.QPushButton('Push Me')
	l = QtWidgets.QLabel('Look at Me!')
	
	h_box = QtWidgets.QHBoxLayout()
	h_box.addStretch()
	h_box.addWidget(l)
	h_box.addStretch()
	v_box = QtWidgets.QVBoxLayout()
	v_box.addWidget(b)
	v_box.addLayout(h_box)
	w.setLayout(v_box)
	
	#b.setText()
	#l.setText()
	#b.move(100,50)
	#l.move(110, 100)
	
	w.setWindowTitle("PyQt5Lesson 2")
	
	
	#w.setGeometry(100,100,300,200) #position x, y, width, height
	#l1.move(100, 20) #move label x, y position
	#l2.move(120, 90)
	
	
	w.show()
	sys.exit(app.exec_())
window()
	
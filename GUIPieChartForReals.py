import sys
import os
import csv
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
QApplication, QWidget, QLabel, QFileDialog, qApp)
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt


class GUIPieChartMaker(QWidget):
	def __init__(self):
		super().__init__()
		
		self.init_ui()
	
	def init_ui(self):
		#Create all UI Elements
		self.le = QLineEdit()
		self.btn_browse = QPushButton('Browse')
		self.btn_quit = QPushButton('Quit')
		self.btn_draw = QPushButton('Draw')
		self.t1 = QLabel('Navigate to your CSV file and click \"Draw\"!')
		
		#Create Horizontal Layout for the LineEdit and Browse Button
		h_box = QHBoxLayout()
		h_box.addWidget(self.le)
		h_box.addWidget(self.btn_browse)
		
		#Create Vertical Layout to make the text look nicer and put
		#it closer to the HLayout with the LineEdit and Browse Button (still ugly)
		v_box_small = QVBoxLayout()
		v_box_small.addWidget(self.t1)
		v_box_small.addLayout(h_box)
		
		#Main Vertical Layout with all elements in it
		v_box = QVBoxLayout()
		v_box.addLayout(v_box_small)
		v_box.addWidget(self.btn_draw)
		v_box.addWidget(self.btn_quit)
		
		#Set main layout, windowsize, and window title
		self.setLayout(v_box)
		self.resize(500,200)
		self.setWindowTitle('ImmaMakaDaPieCharta')
		
		#Call functions when buttons are clicked
		self.btn_quit.clicked.connect(self.quit_action)
		self.btn_browse.clicked.connect(self.browse_action)
		self.btn_draw.clicked.connect(self.draw_action)
		
		self.show()

	def browse_action(self):
		#Browse button opens system file dialog and returns the opened
		#file name into the LineEdit element
		
		filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
		if len(filename[0]) > 0:
			self.le.setText(filename[0])
		else:
			print("File could not be opened...(GUIPieChartMaker.browse_action())")
	
	def draw_action(self):
		#draw_action reads in from csv file and draws the pie chart
		
		#empty lists to add data from csv file
		labels = []
		quantities = []
		sizes = []
		chartTitle = ''
		
		#Get filename from LineEdit
		filename = self.le.text()
		
		#if not empty string, open it and read through it
		if filename != '':
			with open(filename, newline='') as csvfile:
				myFile = csv.reader(csvfile)
				temp = myFile.__next__() #first line should be title in csv file
				chartTitle = temp[0]
				temp = myFile.__next__() #skip column headers
				
				#Add data into the lists 
				for row in myFile:
					labels.append(row[0])
					quantities.append(row[1])
					sizes.append(row[2])
			
			#use first twenty characters of names
			for i in range(len(labels)):
				labels[i] = labels[i][0:20]
			
			#convert quantities to ints
			for i in range(len(quantities)):
				quantities[i] = int(quantities[i])
			
			#convert prices(sizes) to floats
			for i in range(len(sizes)):
				sizes[i] = sizes[i].lstrip('$US')
				sizes[i] = float(sizes[i])
			
			#draw chart
			plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
			plt.title(chartTitle)
			plt.axis('equal')
			plt.show()
			
		else:
			print("Invalid filename for GUIPieChartMaker.draw_action()")
	
	def quit_action(self):
		#Quit application
		qApp.quit()
		



#Create application loop
app = QApplication(sys.argv)
piechartmaker = GUIPieChartMaker()
sys.exit(app.exec_())
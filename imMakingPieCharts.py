import matplotlib.pyplot as plt
import csv

labels = [] 
quantities = []
sizes = [] #prices

with open('dec2017rb.csv', newline='') as csvfile:
	myFile = csv.reader(csvfile)
	temp = myFile.__next__()
	title = temp[0]
	temp = myFile.__next__() #just skip the column headers for now
	
	for row in myFile:
		labels.append(row[0])
		quantities.append(row[1])
		sizes.append(row[2])
		

#print("Labels: ", labels, '\n', "Quantities: ", quantities, '\n', "Sizes: " , sizes)

#just use first twenty characters of names
for i in range(0, len(labels)):
	labels[i] = labels[i][0:20]
	

#change quantities to ints 
for i in range(0, len(quantities)):
	quantities[i] = int(quantities[i])

#change prices(sizes) to floats
for i in range(0, len(sizes)):
	sizes[i] = sizes[i].lstrip('US$')
	sizes[i] = float(sizes[i])


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#plt.legend()
plt.title(title)
plt.axis('equal')
plt.tight_layout()
plt.show()


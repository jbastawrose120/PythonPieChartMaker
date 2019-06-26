import matplotlib.pyplot as plt

#change these 2 variables to suit your needs
nPass = 5857 
nFail = 1362
nParam = 3124

plt.rcParams.update({'font.size': 12}) #adjust font size; not really needed

plt.pie([nPass, nFail, nParam],
        #colors=["green","red"],
        labels=["Pass", "Fail", "Param"],
        autopct='%1.1f%%', 
        startangle=90,
		explode=(0.1,0,0)
		)

plt.axis('equal') #ensure pie is round
plt.show()
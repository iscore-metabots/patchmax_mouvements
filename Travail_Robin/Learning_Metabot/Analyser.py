import os, sys
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def Analyser(src, dst):
	Tmps = [[],[],[],[],[],[],[],[],[],[],[],[]]
	Motor = [[],[],[],[],[],[],[],[],[],[],[],[]]
	for ligne in src:
		donnees = ligne.rstrip('\n\r').split(" ")
			
		Tmps[int(donnees[1])] = Tmps[int(donnees[1])] + [int(donnees[0])]
		
		Motor[int(donnees[1])] = Motor[int(donnees[1])] + [float(donnees[2])]

	f = []
	for motor in range(len(Motor)):
		plt.plot(Tmps[motor],Motor[motor])
		f = f + [interp1d(Tmps[motor], Motor[motor], kind='cubic')]

	plt.show()





if len(sys.argv) != 2:
     print "Usage : python Analyser.py <source>"
else:
	# Ouverture du fichier source
	source = open(sys.argv[1], "r")
	
	# Ouverture du fichier destination
	name = sys.argv[1].split(".")
	dst = name[0] + ".cspl"
	destination = open(dst, "w")

	try:
		# Appeler la fonction de traitement
		Analyser(source, destination)
	finally:
		destination.close()
		source.close()
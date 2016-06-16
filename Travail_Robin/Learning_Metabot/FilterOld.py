import os, sys

def filtrer(src, dst):
	entete = ""
	time = 0
	motor = 1
	res = ""
	OldM = [999.0,999.0,999.0,999.0,999.0,999.0,999.0,999.0,999.0,999.0,999.0,999.0]
	while(entete != "The learning mode will be enabled, you'll need to reboot the board to return to normal operation"):
		entete = src.readline().rstrip('\n\r')
	
	for ligne in src:
		donnees = ligne.rstrip('\n\r').split(" ")
		if ((donnees[1] != "") and OldM[int(donnees[0])] != float(donnees[1])):
			res = res + str(time) + " " + donnees[0] + " " + donnees[1] + '\n'
			OldM[int(donnees[0])] = float(donnees[1])
		if donnees[0] == "11":
			dst.write(res)
			res = ""
			time = time+1

	return





if len(sys.argv) != 2:
     print "Usage : python Analyser.py <source>"
else:
	# Ouverture du fichier source
	source = open(sys.argv[1], "r")
	 
	# Ouverture du fichier destination
	name = sys.argv[1].split(".")
	dst = name[0] + ".data"
	destination = open(dst, "w")
	
	try:
		# Appeler la fonction de traitement
		filtrer(source, destination)
	finally:
		destination.close()
		source.close()
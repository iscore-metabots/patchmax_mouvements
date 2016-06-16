import os, sys

def filtrer(src, dst):
	entete = ""
	res = "specialmove\nmotor1"
	while(entete != "The learning mode will be enabled, you'll need to reboot the board to return to normal operation"):
		entete = src.readline().rstrip('\n\r')
	
	for ligne in src:
		donnees = ligne.rstrip('\n\r').split(" ")
		try:
			float(donnees[1])
			res = res + " " + donnees[1]
		except Exception, e:
			pass
		if donnees[0] == "5":
			res = res + '\n'
			dst.write(res)
			res = "motor2"
		if donnees[0] == "11":
			res = res + '\n'
			dst.write(res)
			res = "motor1"

	return





if len(sys.argv) != 2:
     print "Usage : python Filter2.py <source>"
else:
	# Ouverture du fichier source
	source = open(sys.argv[1], "r")
	 
	# Ouverture du fichier destination
	name = sys.argv[1].split(".")
	dst = name[0] + ".1.txt"
	destination = open(dst, "w")
	
	try:
		# Appeler la fonction de traitement
		filtrer(source, destination)
	finally:
		destination.close()
		source.close()
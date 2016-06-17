import os, sys, serial
from time import sleep

def execute(src, serial):
	for ligne in src:
		serial.write(ligne)
		sleep(0.01)

if len(sys.argv) != 3:
     print "Usage : python Move.py <source> <port>"
else:
	# Ouverture du fichier source
	source = open(sys.argv[1], "r")

	ser= serial.Serial(sys.argv[2])
	print(ser.name)

	execute(source, ser)

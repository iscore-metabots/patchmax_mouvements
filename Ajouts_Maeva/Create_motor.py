import os, sys

def filter1(src, dst):
    entete = ""
    res = "motor"
    while(entete != "The learning mode will be enabled, you'll need to reboot the board to return to normal operation"):
        entete = src.readline().rstrip('\n\r')

    for ligne in src:
        donnees = ligne.rstrip('\n\r').split(" ")
        if(donnees[0] == "11"):
            res = res + " " + donnees[1] + '\n'
            dst.write(res)
            res = "motor"
        else:
            res = res + " " + donnees[1]



if len(sys.argv) != 2:
    print "Usage : python Filter1.py <source>"
else:
    # Ouverture du fichier source
    source = open(sys.argv[1], "r")
        
    # Ouverture du fichier destination
    name = sys.argv[1].split(".")
    dst = name[0] + ".motor.txt"
    destination = open(dst, "w")
        
    try:
    # Appeler la fonction de traitement
        filter1(source, destination)
    finally:
        destination.close()
        source.close()
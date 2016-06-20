import os, sys


def clear(source, destination):
    src = open(source, "r")
    dst = open(destination, "w")
    # Recopiage de l'entete "specialmove"
    entete = ""
    while(entete != "specialmove"):
        entete = src.readline().rstrip('\n\r')
    dst.write("specialmove\n")
    
    # Recopiage de la premiere ligne
    ligne_courante = src.readline()
    dst.write(ligne_courante)

    # Parcours du fichier
    for ligne in src:
        ligne_suivante = ligne.rstrip('\n').split(" ")
        taille = len(ligne_suivante)
        res = ""
        nb_valeurs_identiques = 0

        # Suppression des lignes identiques
        for i in range(1,taille):
            if(ligne_suivante[i] == ligne_courante[i]):
                nb_valeurs_identiques = nb_valeurs_identiques + 1;

        # Ecriture du fichier destination
        if(nb_valeurs_identiques <= taille/2):
            res = ligne_suivante[0]
            for i in range(1,taille):
                res = res + " " + ligne_suivante[i]
            res = res + '\n'
            dst.write(res)
            ligne_courante = ligne_suivante
        else:
            ligne_courante = ligne_suivante

    src.close()
    dst.close()
    return


    
"""
if len(sys.argv) != 2:
    print "Usage: python Clear.py <source>"
else:
    # Ouverture du fichier source
    source = open(sys.argv[1], "r")

    # Ouverture du fichier destination
    name = sys.argv[1].split(".")
    dest = name[0] + "_cleared.txt"
    destination = open(dest, "w")

    try:
        #Appel fonction
        clear(source, destination)

    finally:
        # Fermeture des fichiers
        source.close()
        destination.close()
"""

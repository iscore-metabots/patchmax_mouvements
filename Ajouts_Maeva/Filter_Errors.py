import os, sys

def filter_errors(source, destination):
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
    
        # Suppression des erreurs de calcul (-139.16 ou 139.16)
        for i in range(1,taille):
            if(ligne_suivante[i] == '-139.16' or ligne_suivante[i] == '139.16'):
                ligne_suivante[i] = ligne_courante[i]

        # Ecriture du fichier destination (apres suppression des erreurs)
        res = ligne_suivante[0]
        for i in range(1,taille):
            res = res + " " + ligne_suivante[i]
        res = res + '\n'
        dst.write(res)
        ligne_courante = ligne_suivante

    src.close()
    dst.close()
    return




"""
if len(sys.argv) != 2:
    print "Usage: python Filter_Calc_Errors.py <source>"
else:
    # Ouverture du fichier source
    source = open(sys.argv[1], "r")

    # Ouverture du fichier destination
    name = sys.argv[1].split(".")
    dest = name[0] + "_filtered.txt"
    destination = open(dest, "w")

    try:
        # Appel de la fonction de tri
        filter_errors(source, destination)

    finally:
        # Fermeture des fichiers
        destination.close()
        source.close()
"""

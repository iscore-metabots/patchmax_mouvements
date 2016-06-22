import os, sys


def clear(source, destination):
    src = open(source, "r")
    dst = open(destination, "w")
    # Recopiage de l'entete "specialmove"
    entete = ""
    while(entete != "specialmove"):
        entete = src.readline().rstrip('\n\r')
    dst.write("specialmove\n")
    
    # Recopiage des deux premieres lignes
    ligne1 = src.readline()
    ligne2 = src.readline()
    dst.write(ligne1)
    dst.write(ligne2)

    # Parcours du fichier
    for ligne in src:
        ligne3 = ligne.rstrip('\n').split(" ")
        taille = len(ligne3)
        res = ""
        nb_valeurs_identiques = 0

        # Suppression des lignes identiques
        for i in range(1,taille):
            if(ligne3[i] == ligne1[i]):
                nb_valeurs_identiques = nb_valeurs_identiques + 1;

        # Ecriture du fichier destination
        if(nb_valeurs_identiques <= taille/2):
            res = ligne3[0]
            for i in range(1,taille):
                res = res + " " + ligne3[i]
            res = res + '\n'
            dst.write(res)
            ligne1 = ligne2
            ligne2 = ligne3
        else:
            ligne1 = ligne2
            ligne2 = ligne3

    src.close()
    dst.close()
    return

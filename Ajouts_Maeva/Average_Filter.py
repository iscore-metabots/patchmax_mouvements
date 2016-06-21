import os, sys

def average_filter(source, destination, eps = 0.5):
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

    ligne_courante = ligne_courante.rstrip('\n').split(" ")

    # Parcours du fichier
    for ligne in src:
        ligne_suivante = ligne.rstrip('\n').split(" ")
        taille = len(ligne_suivante)
        res = ""
        
        # Recopiage de la meme valeur si difference <= eps
        for i in range(1,taille):
            if(abs(float(ligne_suivante[i]) - float(ligne_courante[i]))<= eps):
                ligne_suivante[i] = ligne_courante[i]

        # Ecriture du fichier destination
        res = ligne_suivante[0]
        for i in range(1,taille):
            res = res + " " + ligne_suivante[i]
        res = res + '\n'
        dst.write(res)
        ligne_courante = ligne_suivante

    src.close()
    dst.close()
    return

import os, sys

def extreme(source, id_moteur, taille_fichier):
    src = open(source, "r")
    min_val = 0
    max_val = 0
    
    # Avancee jusqu'a ligne depart
    src.readline()

    # Stockage des valeurs du moteur
    valeurs_moteur = []
    for i in range(taille_fichier-1):
        ligne = src.readline().rstrip('\n').split(" ")
        valeurs_moteur = valeurs_moteur + [float(ligne[id_moteur])]
        if(float(ligne[id_moteur]) < min_val):
            min_val = float(ligne[id_moteur])
        if(float(ligne[id_moteur]) > max_val):
            max_val = float(ligne[id_moteur])

    print "\nmoteur" + str(id_moteur)
    print "MIN : " + str(min_val)
    print "MAX : " + str(max_val)
        
    src.close()
    return



for i in range(1,13):
    extreme("txt/test_interpolation.txt",i, 160)        





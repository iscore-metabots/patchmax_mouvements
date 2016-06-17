import os, sys
import numpy as np



def interpolation(id_moteur, ligne_depart, ligne_arrivee, source):
    valeurs_moteur = []

    # Ouverture fichier source
    src = open(source,"r")

    # Avancee jusqu'a ligne depart
    for i in range(ligne_depart):
        src.readline()

    # Stockage des valeurs du moteur
    for i in range(ligne_depart, ligne_arrivee + 1):
        ligne = src.readline().rstrip('\n').split(" ")
        valeurs_moteur = valeurs_moteur + [ligne[id_moteur]]

    # Temps
    temps = np.arange(ligne_arrivee - ligne_depart + 1)
    print temps




interpolation(4,2,7, "screenlog.motor.txt")



import os, sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



def interpolation(id_moteur, ligne_depart, ligne_arrivee, source):

    # Ouverture fichier source
    src = open(source,"r")

    # Avancee jusqu'a ligne depart
    for i in range(ligne_depart):
        src.readline()


    # Stockage des valeurs du moteur
    valeurs_moteur = []
    for i in range(ligne_depart, ligne_arrivee + 1):
        ligne = src.readline().rstrip('\n').split(" ")
        valeurs_moteur = valeurs_moteur + [ligne[id_moteur]]

    # Temps
    temps = np.arange(ligne_arrivee - ligne_depart + 1)

    # Interpolation
    f1 = interp1d(temps, valeurs_moteur) # lineaire
    f2 = interp1d(temps, valeurs_moteur, kind='cubic') #cubique

    # Affichage
    xnew = np.linspace(ligne_depart, ligne_arrivee-1, ligne_arrivee*10)
    plt.plot(temps, valeurs_moteur, 'o', xnew, f1(xnew), '.', xnew, f2(xnew), '-')
    plt.show()

    # Valeur de retour = interpolation cubique
    return f2




interpolation(1,1,600, "NAME_interpolation.txt")
interpolation(2,1,600, "NAME_interpolation.txt")
interpolation(3,1,600, "NAME_interpolation.txt")
interpolation(4,1,600, "NAME_interpolation.txt")
interpolation(5,1,600, "NAME_interpolation.txt")
interpolation(6,1,600, "NAME_interpolation.txt")


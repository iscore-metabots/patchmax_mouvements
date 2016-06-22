import os, sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def lissage(Lx, Ly, p):
    Lxout=[]
    Lyout=[]
    Lxout= Lx[p: -p]
    for i in range(p, len(Ly)-p):
        val = 0
        for k in range(2*p):
            val += float(Ly[i-p+k])
        Lyout.append(val/2/p)
    return Lxout, Lyout
    

def interpolation(id_moteur, ligne_depart, ligne_arrivee, source, k):

    # Ouverture fichier source
    src = open(source,"r")

    # Avancee jusqu'a ligne depart
    for i in range(1, ligne_depart):
        src.readline()

    # Stockage des valeurs du moteur
    valeurs_moteur = []
    for i in range(ligne_depart, ligne_arrivee + 1):
        ligne = src.readline().rstrip('\n').split(" ")
        valeurs_moteur = valeurs_moteur + [ligne[id_moteur]]

    # Temps
    temps = np.arange(ligne_arrivee - ligne_depart + 1)

    temps, valeurs_moteur = lissage(temps,valeurs_moteur,k)

    # Interpolation
    f2 = interp1d(temps, valeurs_moteur, kind='cubic') #cubique

    # Affichage
    fig = plt.figure()
    xnew = np.linspace(k, ligne_arrivee - ligne_depart-k, ligne_arrivee*10)
    plt.plot(xnew, f2(xnew), '-', temps, valeurs_moteur, '.')
    name = "motor" + str(id_moteur) + ".png"
    fig.savefig(name)
    print "%s : DONE" % name
    

    # Valeur de retour = interpolation cubique
    return f2

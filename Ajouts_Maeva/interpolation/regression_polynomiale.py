import numpy as np
import matplotlib.pyplot as plt

"""
c = np.polyfit(x,y,d)
-> c = tab des coefs du polynome de degre d
"""


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




def regression(id_moteur, ligne_depart, ligne_arrivee, source, degre, liss_param):

    # Ouverture fichier source
    src = open(source,"r")

    # Avancee jusqu'a ligne depart
    for i in range(1, ligne_depart):
        src.readline()

    # Stockage des valeurs du moteur
    valeurs_moteur = []
    for i in range(ligne_depart, ligne_arrivee + 1):
        #print i
        ligne = src.readline().rstrip('\n').split(" ")
        #print ligne
        valeurs_moteur = valeurs_moteur + [ligne[id_moteur]]

    # Temps
    temps = np.arange(ligne_arrivee - ligne_depart + 1)

    # Conversion en flottants
    for i in range(len(valeurs_moteur)):
        valeurs_moteur[i] = float(valeurs_moteur[i])

    # Lissage
    temps, valeurs_moteur = lissage(temps,valeurs_moteur, liss_param)
        
    # Regression
    coefs = np.polyfit(temps, valeurs_moteur, degre)
    polynome = np.poly1d(coefs)
    
    # Affichage
    fig = plt.figure()
    xnew = np.linspace(2, ligne_arrivee-ligne_depart -1, ligne_arrivee*10)
    plt.plot(temps, valeurs_moteur, '.', xnew, polynome(xnew), '-')
    name = "motor" + str(id_moteur) + ".png"
    fig.savefig(name)
    print "%s : DONE" % name

    # Valeur de retour = coefficients de le regression polynomiale
    return coefs




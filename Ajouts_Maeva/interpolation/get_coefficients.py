import os, sys

import regression_polynomiale # fonction regression


def entire_regression(source, degree):

    # Get size
    src = open(source, "r")
    taille = 0
    for line in src:
        taille +=1
    src.close()

    # Get coefs
    coefs = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for moteur in range(0,12):
        coefs[moteur] = regression_polynomiale.regression(moteur+1,2,taille-1,source,degree,20,0)
        # toujours commencer ligne 2 (evite "specialmove")
        # degree est le degre du polynome
        # 20 est le coefficient du lissage
        # le 0 final signifie qu'on ne cree pas de graphes
    return coefs
    

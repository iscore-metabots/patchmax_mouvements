import os, sys

import regression_polynomiale # fonction regression


if len(sys.argv) != 3:
    print "Usage: python generate_graphs.py <txt/source_interpolation.txt> <degree of the polynomial-regression>"
else:
    source = sys.argv[1]
    src = open(source, "r")
    taille = 0
    for line in src:
        taille += 1
    src.close()

    degree = int(sys.argv[2])

    print("Drawing graphs...\n")
    for moteur in range(1,13):
        regression_polynomiale.regression(moteur,2,taille-1,source,degree,20,1)
        # toujours commencer ligne 2 (evite "specialmove")
        # degree est le degre du polynome
        # 20 est le coefficient du lissage
        # le 1 final signifie qu'on cree les graphes
    print("\nDrawing ended successfully\n")

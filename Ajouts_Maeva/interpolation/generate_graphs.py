import os, sys

import regression_polynomiale # fonction regression


if len(sys.argv) != 2:
    print "Usage: python generate_graphs.py <source_interpolation.txt>"
else:
    source = sys.argv[1]
    src = open(source, "r")
    taille = 0;
    for line in src:
        taille += 1;
    src.close()

    print("Drawing graphs...\n")
    for i in range(1,13):
        regression_polynomiale.regression(i,2,taille-1,source,10,20)
        # toujours commencer ligne 2 (evite "specialmove")
        # 10 est le degre du polynome
        # 70 est le coefficient du lissage
    print("\nDrawing ended successfully\n")

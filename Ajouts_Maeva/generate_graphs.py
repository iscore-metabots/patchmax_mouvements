import os, sys

import interpolation # fonction interpolation


if len(sys.argv) != 2:
    print "Usage: python generate_graphs.py <source>"
else:
    source = sys.argv[1]
    src = open(source, "r")
    taille = 0;
    for line in src:
        taille += 1;
    src.close()

    print("Drawing graphs...\n")
    for i in range(1,13):
        interpolation.interpolation(i,2,taille-1,source)
    print("\nDrawing ended successfully\n")

import os, sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 3:
    print("Usage: python compare_graphs.py <txt/source_initial_coefficients.txt> <txt/source_modified_coefficients.txt>")
    
else:
    initial = open(sys.argv[1], "r")
    modified = open(sys.argv[2], "r")

    coefs_initial = [[],[],[],[],[],[],[],[],[],[],[],[]]
    coefs_modified = [[],[],[],[],[],[],[],[],[],[],[],[]]

    name = sys.argv[1].split("/")[1].split("_")[0]
    name_interpolation = "txt/" + name + "_interpolation.txt"
    s = open(name_interpolation, "r")
    taille = 0
    for line in s:
        taille += 1
        

    i = 0
    for line in initial:
        motor = line.rstrip('\n\r').split(" ")
        for k in range(1, len(motor)):
            coefs_initial[i] = coefs_initial[i] + [float(motor[k])]
        i += 1

    j = 0
    for line2 in modified:
        motor = line2.rstrip('\n\r').split(" ")
        for k in range(1, len(motor)):
            coefs_modified[j] = coefs_modified[j] + [float(motor[k])]
        j += 1

    print("\nGraphs comparison being calculated ...\n")
    for i in range(len(coefs_initial)):
        fig = plt.figure()
        l = taille
        x = np.linspace(2, l-1, l*10)
        init = np.poly1d(coefs_initial[i])
        modif = np.poly1d(coefs_modified[i])
        plt.plot(x, init(x), '-', x, modif(x), '--')
        name = "graph_comparison/motor" + str(i+1) + ".png"
        fig.savefig(name)
        print("%s : DONE" % name)
    print("\nAll graphs have been calculated.\n")


    initial.close()
    modified.close()

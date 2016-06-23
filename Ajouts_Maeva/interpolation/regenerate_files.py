import os, sys

if len(sys.argv) != 2:
    print("Usage: python regenerate_files.py <txt/source_coefs.txt> <degre> <nombre_lignes_initial> <temps_total_sec>")

else:
    source = open(sys.argv[1], "r")
    degree = int(sys.argv[2])
    taille = int(sys.argv[3])
    coefs = [[],[],[],[],[],[],[],[],[],[],[],[]]

    # Recuperation coefs
    i = 0
    for line in source:
        motor = line.rstrip('\n\r').split(" ")
        for k in range(1, len(motor)):
            coefs[i] = coefs[i] + [float(motor[k])]
        i += 1

    # Creation polynomes
    polynomes = []
    for i in range(len(coefs)):
        polynomes[i] = np.poly1d(coefs[i])

    # Creation du fichier destination
    src = sys.argv[1].split("_")
    name = src[0]
    dst = "interp_" + name + ".txt"
    destination = open(dst, "w")

    # Constantes utiles
    nb_lignes_initial = taille
    nb_valeurs = taille * 10

    # Ecriture du fichier destination
    destination.write("specialmove\n")
    for i in range(taille):
        res = "motor1"
        for j in range(1,len(polynomes)/2 + 1):
            res = res + " " + str(polynomes[j]())


    destination.close()
    source.close()

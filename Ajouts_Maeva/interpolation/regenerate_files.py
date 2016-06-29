import os, sys
import numpy as np

if len(sys.argv) != 3:
    print("Usage: python regenerate_files.py <txt/source_initial||modified_coefficients.txt> <nombre lignes dans txt/mouv_interpolation.txt>")

else:
    source = open(sys.argv[1], "r")
    taille = int(sys.argv[2])
    coefs = [[],[],[],[],[],[],[],[],[],[],[],[]]
    max_value = 150
    min_value = -150

    # Recuperation coefs
    i = 0
    for line in source:
        motor = line.rstrip('\n\r').split(" ")
        for k in range(1, len(motor)):
            coefs[i] = coefs[i] + [float(motor[k])]
        i += 1

    # Creation polynomes
    polynomes = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(coefs)):
        p = np.poly1d(coefs[i])
        polynomes[i] = p

    # Creation des fichiers destination
    src = sys.argv[1].split("_")
    name = src[0].split("/")[1]
    dst1 = "interpolated_txt/interp_" + name + "12.txt"
    destination1 = open(dst1, "w")
    dst2 = "interpolated_txt/interp_" + name + ".txt"
    destination2 = open(dst2, "w")

    # Constantes utiles
    precision = 10
    temps_max = taille
    nb_valeurs = precision * temps_max
    intervalle = (temps_max * 1.0) / nb_valeurs
    tempsEcoule = 0

    # Ecriture du fichier destination
    destination1.write("specialmove\n")
    destination2.write("specialmove\n")
    for i in range(nb_valeurs):
        if(i>=20*precision and i<=nb_valeurs-20*precision):
            res2 = "motor"
            res = "motor1"
            for j in range(len(polynomes)/2):
                if(polynomes[j](tempsEcoule) < min_value):
                    res = res + " " + str(min_value)
                    res2 = res2 + " " + str(min_value)
                elif(polynomes[j](tempsEcoule) > max_value):
                    res = res + " " + str(max_value)
                    res2 = res2 + " " + str(max_value)
                else:
                    res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                    res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))
                    
            res = res + '\n'
            destination1.write(res)
            res = "motor2"
            
            for j in range(len(polynomes)/2, len(polynomes)):
                if(polynomes[j](tempsEcoule) < min_value):
                    res = res + " " + str(min_value)
                    res2 = res2 + " " + str(min_value)
                elif(polynomes[j](tempsEcoule) > max_value):
                    res = res + " " + str(max_value)
                    res2 = res2 + " " + str(max_value)
                else:
                    res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                    res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))
                
            res = res + '\n'
            res2 = res2 + '\n'
            destination1.write(res)
            destination2.write(res2)
            tempsEcoule += intervalle
            
        else:
            tempsEcoule += intervalle
            
    destination1.close()
    destination2.close()
    source.close()

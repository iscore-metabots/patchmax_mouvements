import os, sys
import numpy as np

if len(sys.argv) != 2:
    print("Usage: python regenerate_files.py <txt/source_initial||modified_coefficients.txt>")

else:
    source = open(sys.argv[1], "r")
    coefs = [[],[],[],[],[],[],[],[],[],[],[],[]]
    min_value0 = -96
    max_value0 = 97
    min_value1 = -98
    max_value1 = 110
    min_value2 = -134
    max_value2 = 145

    name = sys.argv[1].split("/")[1].split("_")[0]
    name_interpolation = "txt/" + name + "_interpolation.txt"
    s = open(name_interpolation, "r")
    taille = 0
    for line in s:
        taille += 1
    

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
    precision = 1
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
                if(j%3 == 0):
                    if(polynomes[j](tempsEcoule) < min_value0):
                        res = res + " " + str(min_value0)
                        res2 = res2 + " " + str(min_value0)
                    elif(polynomes[j](tempsEcoule) > max_value0):
                        res = res + " " + str(max_value0)
                        res2 = res2 + " " + str(max_value0)
                    else:
                        res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                        res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))
                    
                if(j%3 == 1):
                    if(polynomes[j](tempsEcoule) < min_value1):
                        res = res + " " + str(min_value1)
                        res2 = res2 + " " + str(min_value1)
                    elif(polynomes[j](tempsEcoule) > max_value1):
                        res = res + " " + str(max_value1)
                        res2 = res2 + " " + str(max_value1)
                    else:
                        res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                        res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))
                        
                if(j%3 == 2):
                    if(polynomes[j](tempsEcoule) < min_value2):
                        res = res + " " + str(min_value2)
                        res2 = res2 + " " + str(min_value2)
                    elif(polynomes[j](tempsEcoule) > max_value2):
                        res = res + " " + str(max_value2)
                        res2 = res2 + " " + str(max_value2)
                    else:
                        res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                        res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))

                    
            res = res + '\n'
            destination1.write(res)
            res = "motor2"
            
            for j in range(len(polynomes)/2, len(polynomes)):
                if(j%3 == 0):
                    if(polynomes[j](tempsEcoule) < min_value0):
                        res = res + " " + str(min_value0)
                        res2 = res2 + " " + str(min_value0)
                    elif(polynomes[j](tempsEcoule) > max_value0):
                        res = res + " " + str(max_value0)
                        res2 = res2 + " " + str(max_value0)
                    else:
                        res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                        res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))
                    
                if(j%3 == 1):
                    if(polynomes[j](tempsEcoule) < min_value1):
                        res = res + " " + str(min_value1)
                        res2 = res2 + " " + str(min_value1)
                    elif(polynomes[j](tempsEcoule) > max_value1):
                        res = res + " " + str(max_value1)
                        res2 = res2 + " " + str(max_value1)
                    else:
                        res = res + " " + str(round(polynomes[j](tempsEcoule),2))
                        res2 = res2 + " " + str(round(polynomes[j](tempsEcoule),2))
                        
                if(j%3 == 2):
                    if(polynomes[j](tempsEcoule) < min_value2):
                        res = res + " " + str(min_value2)
                        res2 = res2 + " " + str(min_value2)
                    elif(polynomes[j](tempsEcoule) > max_value2):
                        res = res + " " + str(max_value2)
                        res2 = res2 + " " + str(max_value2)
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

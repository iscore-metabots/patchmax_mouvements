import os, sys, serial
import numpy as np
from time import sleep

def send_line(line,serial):
    serial.write(line)
    sleep(0.01)




    
if len(sys.argv) != 4:
    print("Usage: python direct_send.py <txt/source_coefficients.txt> <nombre lignes dans txt/mouv_interpolation.txt> <port>")

else:
    ser = serial.Serial(sys.argv[3])
    source = open(sys.argv[1], "r")
    taille = int(sys.argv[2])
    coefs = [[],[],[],[],[],[],[],[],[],[],[],[]]
    max_value = 350
    min_value = -350

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
        
    # Constantes utiles
    precision = 10
    temps_max = taille
    nb_valeurs = precision * temps_max
    intervalle = (temps_max * 1.0) / nb_valeurs
    tempsEcoule = 0


    # Envoi des lignes
    send("specialmove",ser)
    for i in range(nb_valeurs):
        if(i>=20*precision and i<=nb_valeurs-20*precision):
            res = "motor1"
            for j in range(len(polynomes)/2):
                if(polynomes[j](tempsEcoule) < min_value):
                    res = res + " " + str(min_value)
                elif(polynomes[j](tempsEcoule) > max_value):
                    res = res + " " + str(max_value)
                else:
                    res = res + " " + str(round(polynomes[j](tempsEcoule),2))
            res = res + '\n'
            send_line(res,ser)
            res = "motor2"
            
            for j in range(len(polynomes)/2, len(polynomes)):
                if(polynomes[j](tempsEcoule) < min_value):
                    res = res + " " + str(min_value)
                elif(polynomes[j](tempsEcoule) > max_value):
                    res = res + " " + str(max_value)
                else:
                    res = res + " " + str(round(polynomes[j](tempsEcoule),2))
            res = res + '\n'
            send_line(res,ser)
            tempsEcoule += intervalle
    
    ser.close()
    source.close()

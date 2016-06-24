import os, sys, serial
import numpy as np
from time import sleep

def send_line(line,serial):
    serial.write(line)
    sleep(0.01)


if len(sys.argv) != 4:
    print("Usage: python direct_send.py <txt/source_coefficients.txt> <nombre_lignes_initial> <port>")

else:
    ser = serial.Serial(sys.argv[3])
    source = open(sys.argv[1], "r")
    taille = int(sys.argv[2])
    coefs = [[],[],[],[],[],[],[],[],[],[],[],[]]

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
        
    # Constante utile
    nb_lignes = taille * 2
    intervalle = (taille * 1.0) / nb_lignes
    tempsEcoule = 0

    # Envoi des lignes
    send("specialmove",ser)
    for i in range(nb_lignes):
        res = "motor1"
        for j in range(len(polynomes)/2):
            res = res + " " + str(polynomes[j](tempsEcoule))
        res = res + '\n'
        send_line(res,ser)
        res = "motor2"
        for j in range(len(polynomes)/2, len(polynomes)):
            res = res + " " + str(polynomes[j](tempsEcoule))
        res = res + '\n'
        send_line(res,ser)
        tempsEcoule += intervalle
    
    ser.close()
    source.close()

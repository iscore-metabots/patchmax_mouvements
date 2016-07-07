import os, sys, serial
from collections import OrderedDict
import numpy as np



def file_size(source):
    src = open(source, "r")
    taille = 0
    for line in src:
        taille += 1
    src.close()
    return taille


def decoup_moteur(id_moteur, source):
    src = open(source,"r")

    #Avancee jusqu'a la ligne de depart
    src.readline() # lecture du "specialmove"

    # Stockage des valeurs du moteur
    valeurs_moteur = []
    for line in src:
        ligne = line.rstrip('\n').split(" ")
        valeurs_moteur = valeurs_moteur + [float(ligne[id_moteur])]


    # Stockage premiere valeur dans dict
    d = OrderedDict()
    d[1] = valeurs_moteur[0]

    
    # Initialisation des variables de parcours
    last_val_in_d = valeurs_moteur[0]
    last_val = valeurs_moteur[1]
    if(abs(d[1] - last_val)<1):
        tendance = 0
    if(d[1]<last_val):
        tendance = 1
    elif(d[1]>last_val):
        tendance = -1
    tendance_generale = tendance
    

    # Parcours
    for i in range(2, len(valeurs_moteur)):
        if(abs(last_val - valeurs_moteur[i])<1):
            tendance = 0
        elif(last_val < valeurs_moteur[i]):
            tendance = 1
        elif(last_val > valeurs_moteur[i]):
            tendance = -1
        if(tendance != tendance_generale):
            if(tendance_generale==0):
                d[i] = last_val_in_d
                tendance_generale = tendance
            else:
                d[i] = last_val # on met la derniere valeur dans d (i car les lignes vont de 1 a n et valeurs_moteur va de 0 a n-1)
                tendance_generale = tendance
                last_val_in_d = last_val
        last_val = valeurs_moteur[i]

    src.close()
    taille_source = file_size(source)
    d[taille_source] = last_val
    return d   # d = {numero_ligne:valeur moteur, n2:v2, n3:v3, etc...}




def decoup_mouv(source):
    tab =[]
    for i in range(1,13):
        tab = tab + [decoup_moteur(i,source)]
    return tab



"""
coefs = np.polyfit(x,y,d)
-> coefs = tab des coefs du polynome de degre d
poly = np.poly1d(coefs)
"""


def decoup_interp_mouv(source):
    tab = [[],[],[],[],[],[],[],[],[],[],[],[]]
    decoup = decoup_mouv(source) # tab de dictionnaires
    for moteur in range(0,12):
        tab_keys = []
        for key in decoup[moteur]:
            tab_keys += [key]
        taille = len(tab_keys)
        for i in range(taille-1):
            x = [tab_keys[i],tab_keys[i+1]]
            y = [decoup[moteur][tab_keys[i]],decoup[moteur][tab_keys[i+1]]]
            coefs = np.polyfit(x,y,1)
            poly = np.poly1d(coefs)
            #
            xnew = np.linspace(tab_keys[i], tab_keys[i+1], tab_keys[i+1] - tab_keys[i])
            ynew = poly(xnew)
            for val in range(len(xnew)):
                tab[moteur] += [round(poly(val),2)]
    return tab




def generate_file(source):

    # Recup valeurs de tous les moteurs
    values = decoup_interp_mouv(source)

    # Creation et ouverture fichier destination
    name = source.split("/")[1].split("_")[0]
    destination = "interpolated_txt/better_interp_" + str(name) + ".txt"
    dst = open(destination, "w")

    # Ecriture premiere ligne
    dst.write("specialmove\n")

    # Recuperation nombre de lignes a generer
    taille = file_size(source)-2

    for ligne in range(taille):
        res = "motor1"
        for i in range(6):
            res = res + " " + str(values[i][ligne])
        res += '\n'
        dst.write(res)
        res = "motor2"
        for i in range(6,12):
            res = res + " " + str(values[i][ligne])
        res += '\n'
        dst.write(res)
    dst.close()



def send_line(line,serial):
    serial.write(line)
    sleep(0.01)


def direct_send(source, port):

    # Recup valeurs de tous les moteurs
    values = decoup_interp_mouv(source)

    # Ouverture Port
    ser = serial.Serial(port)

    # Ecriture premiere ligne
    send_line("specialmove\n",ser)

    # Recuperation nombre de lignes a generer
    taille = file_size(source)-2

    for ligne in range(taille):
        res = "motor1"
        for i in range(6):
            res = res + " " + str(values[i][ligne])
        res += '\n'
        send_line(res,ser)
        res = "motor2"
        for i in range(6,12):
            res = res + " " + str(values[i][ligne])
        res += '\n'
        send_line(res,ser)
    ser.close()    


if len(sys.argv) == 1:
    generate_file("txt/glide_interpolation.txt")
else:
    direct_send("txt/glide_interpolation.txt", sys.argv[1])

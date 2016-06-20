import os, sys

def decoupage_mouv_patte(num_patte, source):

    # Ouverture source
    src = open(source, "r")

    # Stockage moteurs
    if(num_patte>=1 and num_patte<=4):
        moteur1 = (num_patte -1)*3 + 1
        moteur2 = (num_patte -1)*3 + 2
        moteur3 = (num_patte -1)*3 + 3
    else:
        print("Patte non existante")
        return

    # Decoupage selon croissance/decroissance
    

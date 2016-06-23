import os, sys

import get_coefficients # fonction entire_regression


def write_coefs(source, destination, degree):
    coefs = get_coefficients.entire_regression(source, degree)
    
    name = source.split("_")
    destination = name[0] + "_initial_coefficients.txt"
    dst = open(destination, "w")

    for moteur in range(12):
        res = str(moteur + 1)
        for coef in range(degree+1):
            res = res + " " + str(coefs[moteur][coef])
        res = res + '\n'
        dst.write(res)

    dst.close()

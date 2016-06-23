import os, sys

import get_coefficients # fonction entire_regression


def write_coefs(source, destination1, destination2, degree):
    coefs = get_coefficients.entire_regression(source, degree)
    
    dst1 = open(destination1, "w")
    dst2 = open(destination2, "w")

    for moteur in range(12):
        res = str(moteur + 1)
        for coef in range(degree+1):
            res = res + " " + str(coefs[moteur][coef])
        res = res + '\n'
        dst1.write(res)
        dst2.write(res)

    dst1.close()
    dst2.close()

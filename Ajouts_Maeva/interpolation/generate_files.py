import os, sys


import Create_motor # fonction filter1
import Create_motor12 # fonction filter12
import Filter_Errors # fonction filter_errors
import Clear # fonction clear
import Clear2 # fonction clear
import coefficients_textfile # fonction write_coefs


if len(sys.argv) != 3:
    print "Usage: python generate_files.py <nom_mouvement> <degree-of-polynomial-regression>"
else:
    name = "txt/" + sys.argv[1] + ".0"
    os.rename("txt/screenlog.0", name)
    degree = int(sys.argv[2])


    # FICHIERS INTERPOLATION
    # Mets en ligne
    motor = name.split(".")[0] + "_motor.txt"
    Create_motor.filter1(name, motor)

    # Enleve valeurs extremes
    #motor_filtered = motor.split(".")[0] + "_filtered.txt"
    motor_interpolation = name.split(".")[0] + "_interpolation.txt"
    Filter_Errors.filter_errors(motor, motor_interpolation)

    # Enleve lignes identiques
    #motor_interpolation = name.split(".")[0] + "_interpolation.txt"
    #Clear.clear(motor_filtered, motor_interpolation)

    # Cree fichier des coefficients de l'interpolation
    motor_coefficients = name.split(".")[0] + "_initial_coefficients.txt"
    motor_coefs_modified = name.split(".")[0] + "_modified_coefficients.txt"
    coefficients_textfile.write_coefs(motor_interpolation, motor_coefficients, motor_coefs_modified, degree)


    
    # FICHIERS MOUVEMENT
    # Mets en ligne
    motor12 = name.split(".")[0] + "_motor12.txt"
    Create_motor12.filter12(name, motor12)

    # Enleve les valeurs extremes
    #motor12_filtered = motor12.split(".")[0] + "_filtered.txt"
    name_txt = name.split(".")[0] + ".txt"
    Filter_Errors.filter_errors(motor12, name_txt)

    # Enleve lignes identiques
    #name_txt = name.split(".")[0] + ".txt"
    #Clear2.clear(motor12_filtered, name_txt)


    os.remove(motor12)
    #os.remove(motor12_filtered)
    
    os.remove(motor)
    #os.remove(motor_filtered)


import os, sys


import Create_motor # fonction filter1
import Create_motor12 # fonction filter12
import Filter_Errors # fonction filter_errors
import Clear # fonction clear
import Clear2 # fonction clear
import Average_Filter # fonction average_filter



if len(sys.argv) != 2:
    print "Usage: python generate_files.py nom_mouvement"
else:
    name = sys.argv[1] + ".0"
    os.rename("screenlog.0", name)


    # FICHIERS INTERPOLATION
    # Mets en ligne
    motor = name.split(".")[0] + "_motor.txt"
    Create_motor.filter1(name, motor)

    # Enleve valeurs extremes
    motor_filtered = motor.split(".")[0] + "_filtered.txt"
    Filter_Errors.filter_errors(motor, motor_filtered)

    # Enleve lignes identiques
    motor_interpolation = name.split(".")[0] + "_interpolation.txt"
    Clear.clear(motor_filtered, motor_interpolation)

    """
    # Rassemble les valeurs proches
    motor_average = name.split(".")[0] + "_average.txt"
    Average_Filter.average_filter(motor_interpolation, motor_average, 1)"""

    
    # FICHIERS MOUVEMENT
    # Mets en ligne
    motor12 = name.split(".")[0] + "_motor12.txt"
    Create_motor12.filter12(name, motor12)

    # Enleve les valeurs extremes
    motor12_filtered = motor12.split(".")[0] + "_filtered.txt"
    Filter_Errors.filter_errors(motor12, motor12_filtered)

    # Enleve lignes identiques
    name_txt = name.split(".")[0] + ".txt"
    Clear2.clear(motor12_filtered, name_txt)


    os.remove(motor12)
    os.remove(motor12_filtered)
    
    os.remove(motor)
    os.remove(motor_filtered)


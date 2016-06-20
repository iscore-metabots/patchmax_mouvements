import os, sys

if len(sys.argv) != 2:
    print "Usage: python remove_files.py nom_mouvement"
else:
    name = sys.argv[1] + ".0"
    motor = name.split(".")[0] + "_motor.txt"
    motor12 = name.split(".")[0] + "_motor12.txt"
    motor_filtered = motor.split(".")[0] + "_filtered.txt"
    motor12_filtered = motor12.split(".")[0] + "_filtered.txt"
    motor_filtered_cleared = motor_filtered.split(".")[0] + "_cleared.txt"
    motor12_filtered_cleared = motor12_filtered.split(".")[0] + "_cleared.txt"
    
    os.remove(motor)
    os.remove(motor12)
    os.remove(motor_filtered)
    os.remove(motor12_filtered)
    os.remove(motor_filtered_cleared)
    os.remove(motor12_filtered_cleared)
    
    os.rename(name, "screenlog.0")
    

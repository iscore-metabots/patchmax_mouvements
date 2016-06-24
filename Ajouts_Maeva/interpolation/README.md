
## Fonctions Utilisables:

* __python generate_files.py \<nom_mouvement_voulu\> :__   
Nécessite au préalable d'avoir enregistré un mouvement "screenlog.0" dans le répertoire "txt"   
Va créer d'autres fichiers dans le répertoire "txt":      
    * _mouv.0_
    * _mouv.txt_
    * _mouv\_interpolation.txt_
    * _mouv\_initial\_coefficients.txt_
    * _mouv\_modified\_coefficiens.txt_


## Fonctions Annexes:

* __Create_motor.py / Create_motor12.py :__   
Créent les fichiers contenant les valeurs des moteurs à des instants successifs à partir de "screenlog.0"

* __Filter_Errors.py :__  
Enlève les erreurs de calcul produites lors de l'enregistrement

* __Clear.py / Clear2.py :__   
Enlèvent les lignes successives identiques

* __regression_polynomiale.py :__   
Calcule le polynome moyen passant par toutes les valeurs d'un moteur

* __get_coefficients.py :__   
Rassemble les coefficients de tous les polynomes representant l'évolution de chaque moteur

* __coefficients_textfile.py :__   
Ecrit les coefficients du polynome de chaque moteur dans un fichier texte
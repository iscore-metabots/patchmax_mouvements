
## Fonctions Utilisables:

* __python generate_files.py \<nom_mouvement_voulu\> :__   
Nécessite au préalable d'avoir enregistré un mouvement "screenlog.0" dans le répertoire "txt"   
Va créer d'autres fichiers dans le répertoire "txt":      
    * _mouv.0_ : fichier "screenlog.0" renommé
    * _mouv.txt_ : fichier contenant le mouvement prêt à être envoyé
    * _mouv\_interpolation.txt_ : fichier servant au calcul des polynomes représentant le mouvement de chaque moteur
    * _mouv\_initial\_coefficients.txt_ : fichier contenant les coefficients de chaque polynome (un polynome représentant un moteur)
    * _mouv\_modified\_coefficiens.txt_ : fichier identique au fichier précédent, on peut y changer le dernier nombre de chaque ligne (Ce nombre correspond au terme constant du polynome considéré, cela fera ainsi varier l'amplitude du mouvement par rapport à l'amplitude initiale, si on recalcule le mouvement à partir de ce fichier. Attention: Ne pas modifier les autres coefficients!)

* __python generate\_graphs.py \<txt/mouv\_interpolation.txt\> \<degré du polynome voulu\> :__   
Crée pour chaque moteur un graphe représentant les valeurs réelles du moteur et le polynome moyen de degré demandé obtenu par régression polynomiale

* __regenerate_files.py :__   
To be explained soon


* __compare_graphs.py :__   
To be explained soon


* __direct_send.py :__   
To be explained soon




## Ordre d'appel des fonctions:

Appeler _generete\_files.py avant les 4 autres.




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
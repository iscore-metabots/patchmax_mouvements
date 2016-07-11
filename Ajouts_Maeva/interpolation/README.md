
## API - 7 Fonctions Utilisateur:

* __python generate_files.py \<nom_mouvement_voulu\> \<degre du polynome voulu (pour la regression polynomiale)\> :__   
Nécessite au préalable d'avoir enregistré un mouvement "screenlog.0" dans le répertoire "txt"   
Cette fonction crée d'autres fichiers dans le répertoire "__txt__":      
    * _mouv.0_ : fichier "screenlog.0" renommé
    * _mouv.txt_ : fichier contenant le mouvement prêt à être envoyé (envoi avec la fonction Move.py ou par copier/coller dans le "screen")
    * _mouv\_interpolation.txt_ : fichier servant au calcul des polynomes représentant le mouvement de chaque moteur
    * _mouv\_initial\_coefficients.txt_ : fichier contenant les coefficients de chaque polynome (un polynome représentant un moteur)
    * _mouv\_modified\_coefficiens.txt_ : fichier identique au fichier précédent, on peut y changer le dernier nombre de chaque ligne (Ce nombre correspond au terme constant du polynome considéré, cela fera ainsi varier l'amplitude du mouvement par rapport à l'amplitude initiale si on recalcule le mouvement à partir de ce fichier. Attention: Ne pas modifier les autres coefficients!)

* __python generate\_graphs.py \<txt/mouv\_interpolation.txt\> \<degré du polynome voulu\> :__   
Dans le répertoire "__img__", crée pour chaque moteur un graphe représentant les valeurs réelles du moteur et le polynome moyen de degré demandé, obtenu par régression polynomiale.

* __python regenerate_files.py \<txt/mouv_initial_coefficients.txt || txt/mouv_modified_coefficients.txt\> :__   
Crée les fichiers "interp_mouv.txt" et "interp_mouv12.txt" dans le répertoire "__interpolated_txt__".   
On peut l'appeler avec _mouv\_initial\_coefficients.txt_ou _mouv\_modified\_coefficiens.txt_ suivant si l'on veut que le mouvement soit identique à celui que l'on a enregistré (tout en étant "lissé"), ou si on veut en faire varier l'amplitude.     
Le fichier "interp_mouv12.txt" contient le mouvement généré à partir des polynomes (calculés par régression polynomiale et par lissage). Ce fichier peut-être envoyé au Metabot par la fonction Move.py ou par copier/coller dans le "screen".      
Le fichier "interp_mouv.txt" peut être rappelé avec la fonction "generate_graphs" dans le répertoire "__interpolated_txt__" pour visualiser les nouvelles valeurs des moteurs au cours du temps. Les nouveaux graphes seront visibles dans le répertoire "__interpolated_txt/img__".  


* __python compare_graphs.py \<txt/mouv_initial_coefficients.txt\> \<txt/mouv_modified_coefficients.txt\>:__   
Crée dans le répertoire "__graph_comparison__" un graphe pour chaque moteur représentant le polynome initial associé aux valeurs du moteur, et le polynome modifié (en amplitude) par l'utilisateur.


* __python direct_send.py \<txt/mouv_initial||modified_coefficients.txt\> \<port serie\> :__   
Envoie directement le mouvement au Metabot à partir des coefficients du polynome de chaque moteur, et sans créer de fichier texte intermédiraire.   

* __python Move.py \<txt/mouv.txt || interpolated_txt/interp_mouv12.txt\> \<port\>:__   
Envoie le fichier texte au Metabot (fichier texte contenant le mouvement).

* __python decoup_mouv.py \<txt/mouv_interpolation.txt\>__ ou __python decoup_mouv.py \<txt/mouv_interpolation.txt\> \<port serie\>:__  
Fonction qui découpe le mouvement aux endroits où il change de tendance (croissance/décroissance/constance), qui stocke dans un dictionnaire les lignes et les valeurs des moteurs où la croissance/décroissance change, et qui interpole les valeurs successives du dictionnaire.  
La première commande permet de générer le fichier du mouvement (nommé "interp_txt/better_interp_mouv.txt") et de tracer les graphes (dans le répertoire "decoup_mouv") pour chaque moteur, la seconde commande permet d'envoyer directement le mouvement au metabot directement à partir des interpolations et sans créer de fichier texte.  



## Ordre d'appel des fonctions:

Appeler _generete\_files.py_ avant les 6 autres (elle génère les fichiers sur lesquels les autres fonctions se basent).  
Les autres fonctions sont ensuite indépendantes. 




## Fonctions Annexes (appelées par les fonctions ci-dessus):

* __Create_motor.py / Create_motor12.py :__   
Créent les fichiers contenant les valeurs des moteurs à des instants successifs à partir de "screenlog.0"

* __Filter_Errors.py :__  
Enlève les erreurs de calcul produites lors de l'enregistrement

* __Clear.py / Clear2.py :__   
Enlèvent les lignes successives identiques

* __regression_polynomiale.py :__   
Fait un "lissage" des différentes valeurs puis calcule le polynome moyen passant par toutes les valeurs d'un moteur

* __get_coefficients.py :__   
Rassemble les coefficients de tous les polynomes representant l'évolution de chaque moteur

* __coefficients_textfile.py :__   
Ecrit les coefficients du polynome de chaque moteur dans un fichier texte
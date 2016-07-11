
## Enregistrer un mouvement:

* installer firmware Robin (permettant au metabot de comprendre "specialmove", "learning", "motor1" et "motor2")
* lancer commande "sudo screen \<port serie\> 115200"
* lancer commande "ctrl-a H" —> lance l’enregistrement
* lancer commande "learning"
* faire manuellement au robot le mouvement souhaité
* lancer commande "ctrl-a \" (ou fermer le terminal et éteindre le robot) —> stoppe l’enregistrement
* déplacer le fichier "screenlog.0" dans le répertoire "interpolation/txt"
* aller dans le répertoire "interpolation"
* lancer commande "python generate_files.py \<nom_mouvement\> \<degré de l'interpolation\>" —> Le mouvement souhaité est dans le fichier "nom_mouv.txt" (mettre 6 par défaut pour le degré, cela n'entre pas en compte ici)




## Lancer un mouvement (en ligne de commande):

* établir une connection bluetooth avec le metabot (via Bluemanager sur Linux)
* aller dans le répertoire "interpolation"
* lancer commande "python Move.py txt/nom_mouv.txt \<port serie\>"
	



## Lancer un mouvement depuis screen:

* lancer commande "sudo screen \<port serie\> 115200"
* lancer commande "start"
* copier/coller l'intégralité du fichier "interpolation/txt/nom_mouv.txt" dans le screen




## Lancer un mouvement depuis Max/MSP:

* établir une connection bluetooth avec le metabot (Problème: maintient de la connection difficile sur Mac et Windows)
* aller dans le répertoire "Max_IHM" puis "lib_fixe" ou "lib_vitesse" et cliquer sur le mouvement voulu
* deux patchs sont pour l'instant à disposition: mouvement fixe + mouvement dont la vitesse est contrôlable (pour celui dont la vitesse est contrôlable, faire varier le curseur après avoir lancé le mouvement)




## Ajouter un mouvement dans l’interface Max/MSP:

* copier/coller le fichier "interpolation/txt/nom_mouv.txt" dans le répertoire "Max_IHM"
* ouvrir le fichier "Max_IHM/Lib_\<choix\>.maxpat" (choix: fixe ou gestion vitesse)
* copier/coller le modèle de patch
* marquer le nom du nouveau mouvement (le même que le .txt) à la place de "NAME"

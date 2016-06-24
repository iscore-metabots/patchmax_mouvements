
Enregistrer un mouvement:
=========================
* installer firmware Robin (permettant au metabot de comprendre "specialmove", "learning", "motor1" et "motor2")
* lancer commande "sudo screen \<port serie\> 115200"
* lancer commande "ctrl-a H" —> lance l’enregistrement
* lancer commande "learning"
* faire manuellement au robot le mouvement souhaité
* lancer commande "ctrl-a \" (ou fermer le terminal et éteindre le robot) —> stoppe l’enregistrement
* déplacer le fichier "screenlog.0" dans le répertoire "interpolation"
* aller dans le répertoire "interpolation"
* lancer commande "python generate_files.py \<nom_mouvement\>" -> création de fichiers dans le répertoire "txt"




Lancer un mouvement (en ligne de commande):
===========================================
* établir une connection bluetooth avec le metabot
* aller dans le répertoire "interpolation"
* lancer commande "python Move.py txt/nom_mouv.txt \<port serie\>"
	



Lancer un mouvement depuis screen:
==================================
* lancer commande "sudo screen \<port serie\> 115200"
* lancer commande "start"
* copier/coller l'intégralité du fichier "interpolation/txt/nom_mouv.txt" dans le screen




Lancer un mouvement depuis Max/MSP:
===================================
* établir une connection bluetooth avec le metabot
* aller dans le répertoire "Max_IHM" puis "lib_fixe" ou "lib_vitesse" et cliquer sur le mouvement voulu (sera fonctionnel quand la librairie sera créée)
* deux patchs sont pour l'instant à disposition: mouvement fixe + mouvement dont la vitesse est contrôlable




Ajouter un mouvement dans l’interface Max/MSP:
==============================================
* copier/coller le fichier "interpolation/txt/nom_mouv.txt" dans le répertoire "Max_IHM"
* aller dans le répertoire "Max_IHM/Lib_\<choix\>.maxpat" (choix: fixe ou gestion vitesse)
* copier/coller le modèle de patch
* marquer le nom du mouvement (le même que le .txt) à la place de "NAME"

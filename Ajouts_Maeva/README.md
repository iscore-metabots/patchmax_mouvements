
Enregistrer un mouvement:
=========================
	- installer firmware Robin
	- lancer commande "sudo screen /dev/cu.ROBOTISBT-120-SSPDev 115200"
	- lancer commande "ctrl-a H" —> lance l’enregistrement
	- faire manuellement au robot le mouvement souhaité
	- lancer commande "ctrl-a \" (ou fermer le terminal, ou éteindre le robot) —> stoppe l’enregistrement
	- lancer commande "python generate_files.py <nom_mouvement>" -> création de "<nom_mouvement.txt>" + fichier utile à l'interpolation




Lancer un mouvement (en ligne de commande):
===========================================
    - établir une connection bluetooth avec le metabot
    - lancer commande "python Move.py nom_mouv.txt /dev/cu.ROBOTISBT-120-SSPDEV"
	



Lancer un mouvement depuis screen:
==================================
	- lancer commande "sudo screen /dev/cu.ROBOTISBT-120-SSPDev 115200"
	- lancer commande "start"
	- copier/coller le fichier "nom_mouv.txt" dans le screen




Lancer un mouvement depuis Max/MSP:
===================================
    - établir une connection bluetooth avec le metabot
    - aller dans le répertoire "Max_IHM" puis "lib_fixe" ou "lib_vitesse" et cliquer sur le mouvement voulu (sera fonctionnel quand la librairie sera créée)
    - deux patchs sont à disposition: mouvement fixe + mouvement dont la vitesse est contrôlable




Ajouter un mouvement dans l’interface Max/MSP:
==============================================
    - aller dans le répertoire "Max_IHM"
    - copier/coller le modèle de patch (fixe ou vitesse)
    - marquer le nom du mouvement (le même que le .txt) à la place de "NAME"




Modifications à venir:
======================
	- ajout du maintien automatique de la connexion bluetooth avec MAX/MSP
	- mouvements dont les paramètres sont contrôlables par l’utilisateur (ex: amplitude)


Enregistrer un mouvement (fichiers Robin légèrement modifiés + rajout d’une fonction):
======================================================================================
	- installer firmware Robin
	- lancer commande « sudo screen /dev/cu.ROBOTISBT-120-SSPDev 115200»
	- lancer commande « ctrl-a H » —> lance l’enregistrement
	- faire manuellement au robot le mouvement souhaité
	- lancer commande « ctrl-a \ » —> stoppe l’enregistrement
	- renommer fichier « screenlog.0 » en « nom_mouv.log »
	- lancer commande « python Filter2.py nom_mouv.log » —> création « nom_mouv.1.txt »
	- lancer commande « python Filter_Calc_Errors.py nom_mouv.1.txt » —> création « nom_mouv.txt »




Lancer un mouvement (en ligne de commande):
===========================================
    - établir une connection bluetooth avec le metabot
	- lancer commande « python Move.py nom_mouv.txt »
	



Lancer un mouvement depuis screen:
==================================
	- lancer commande « sudo screen /dev/cu.ROBOTISBT-120-SSPDev 115200»
	- lancer commande « start »
	- copier/coller le fichier « nom_mouv.txt » dans le screen




Lancer un mouvement depuis Max/MSP:
===================================
    - établir une connection bluetooth avec le metabot
	- aller dans le répertoire « Max (IHM) » puis « lib_mouvements » et cliquer sur le mouvement voulu (sera fonctionnel quand la librairie sera créée)
	- deux patchs sont à disposition: mouvement fixe + mouvement dont la vitesse est contrôlable




Ajouter un mouvement dans l’interface Max/MSP:
==============================================
	- copier/coller le patch d’un autre mouvement
	- changer les « ancien_nom.txt » en « nom_voulu.txt »
	- changer les « lancer mouv ancien_nom » en « lancer mouv nom_voulu »
	- le nouveau patch est alors fonctionnel




Modifications à venir:
======================
	- ajout du maintien automatique de la connexion bluetooth avec MAX/MSP
	- mouvements dont les paramètres sont contrôlables par l’utilisateur (ex: amplitude)

# Projet de Feu de Foret + Propagation du Virus NSI #2
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

◆ Projet achevé le 8/05/2020 [X]

# À propos

C'est un projet de NSI ( Numérique et Sciences Informatiques ) sur le feu de foret + la propagation du virus en se basant sur l'automate cellulaire, Au début, le code initiale etait déjà écrit ( surtout les fonctions principaux ), puis notre professeur a mis tout le code en nous demandant de l'améliorer. Biensûr, je l'ai pas fait tout seul, je les fait avec un groupe de potes. Le programme est écrit sur le logiciel processing en python.

# Logiciel requis

**•** Processing 3 Python Mode ( **Obligatoire** puisqu'on utilise certaines fonctions du processing qui n'est pas sur python )

# Installation

Après avoir téléchargé le logiciel et ouvert le projet, pour se servir du programme, voici les valeurs des variables que vous pouvez changer facilement.
**IMPORTANT** : Si vous comprenez le language python et la structure de notre projet, vous pouvez le modifer a votre guise, faites-vous plaisir.

# Pour le Feu de Foret

N      = 50 par défaut   # taille du tableau carré

size(600, 600)   # on crée une fenêtre (ex: 600x600)

frameRate(10)    # la boucle draw() sera appelée x fois par secondes

fabrique_la_foret(0.425,0.1) # on se fabrique une jolie forêt

met_le_feu(1)    # ...et on y allume plusieurs foyers

la_foudre_c_cool(0) # nombre de foudre

# Pour la Propagation du Virus

N      = 50

taux_contamination = 0.4

taux_porteur_sains = 0.05

mortalite = 0.02

taux_immunise = 0.01

size(600, 600)   # on crée une fenêtre (ex: 600x600)

frameRate(5)    # la boucle draw() sera appelée x fois par secondes

fallout(1)    # ...et on y allume plusieurs foyers (oui oui on est très créatifs), Allumage d'un certain nombre de porteur sain

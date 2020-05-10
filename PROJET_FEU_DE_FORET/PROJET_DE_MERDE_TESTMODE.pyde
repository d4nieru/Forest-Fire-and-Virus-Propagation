#######################################################
### Simulation de la propagation d'un feu de forêt ####
############################ NSI 2019 - 2020 ########## 

from random import *


#### déclaration des variables "globales" ####
N      = 50   # taille du tableau carré
VIDE   = 0
ARBRE  = 1
CYPRES = 2
CYPRES2 = 3
BRULE  = 4
BRAISE = 5
CENDRE = 6
FOUDRE = 7                                                                
FOUDRE2 = 8
FOUDRE3 = 9
fini = False 
terrain = [[VIDE for c in range(N)] for l in range(N)]
copie_de_terrain = [[VIDE for c in range(N)] for l in range(N)]



def setup(): # Au lancement du programme...
    size(600, 600)   # on crée une fenêtre 800x800
    rectMode(CORNER) # on sera en mode CORNER pour les rectangles
    frameRate(10)    # la boucle draw() sera appelée 20 fois par secondes
    fabrique_la_foret(0.425,0.1) # on se fabrique une jolie forêt
    met_le_feu(1)    # ...et on y allume plusieurs foyers
    la_foudre_c_cool(2) # on fait tomber de la foudre un certain nombre de fois car la foudre, c cool (et ça brûle les arbres, adieu les arbres)

c = 0    
def draw():  # boucle draw(): 10 fois par secondes...
    background(255)                  # on efface l'écran et on le passe en fond blanc
    stroke(0)                        # tracé des traits en noir
    fill(255)                        # remplissage en blanc
    rect(0,0,width-1,height-1)       # on trace un rectangle sur le contour de l'écran
    quadrillage()                    # on réalise le quadrillage  
    affiche_le_terrain()             # on affiche le terrain
    applique_regles_de_propagation() # on applique les règles de propagation

###



###

def fabrique_la_foret (densite, densite2):
    '''peuplement du tableau 'terrain' avec une certaine densité d'arbres'''
    global terrain # pour pouvoir modifier cette variable
    for ligne in range(N):
       for colonne in range(N):
            if random()<=densite-densite2: # si un nombre tiré au hasard est plus petit que "densité" on suppose qu'on est bon # donc on pose un arbre
                terrain[ligne][colonne] = ARBRE
            elif random()<=densite2: # si un nombre tiré au hasard est plus petit que "densité" on suppose qu'on est bon # donc on pose un arbre
                terrain[ligne][colonne] = CYPRES
            else: #sinon
                terrain[ligne][colonne]=VIDE # pas d'arbre
            # ça fait le job car avec cette méthode, densite=1 met toutes les cases à ARBRE et densite=0 aucune.

def met_le_feu(ndf):
    '''Allumage d'un certain nombre de foyers'''
    for i in range(ndf):
        ligne = randint(0, N-1)
        colonne = randint(0, N-1)
        terrain[ligne][colonne] = BRULE

def la_foudre_c_cool(ez):
    for i in range(ez):
        ligne = randint(0, N-1)
        colonne = randint(0, N-1)
        terrain[ligne][colonne] = FOUDRE
        if colonne <= 49:
           terrain[ligne][colonne+1] = FOUDRE
        if colonne >= 1:
           terrain[ligne][colonne-1] = FOUDRE
        if ligne >= 1:
           terrain[ligne-1][colonne] = FOUDRE
        if ligne <= 49:
           terrain[ligne+1][colonne] = FOUDRE

def t(ligne, colonne):
    '''Fonction sentinelle qui vaut le contenu de copie_de_terrain si les coordonnées sont valides et VIDE sinon'''
    if (ligne<0) or (colonne<0) or (ligne>=N) or (colonne >= N) :
        return VIDE
    else :
        return copie_de_terrain[ligne][colonne]
  

def au_moins_un_voisin_en_feu(ligne,colonne):
    '''envoie True si au moins un des voisins de la case ligne,colonne est en feu'''
    if t(ligne-1,colonne-1)==BRULE or t(ligne-1,colonne)==BRULE or t(ligne-1,colonne+1)==BRULE or t(ligne,colonne-1)==BRULE or t(ligne,colonne+1)==BRULE or t(ligne+1,colonne-1)==BRULE or t(ligne+1,colonne)==BRULE or t(ligne+1,colonne+1)==BRULE :
        return True
    return False

def applique_regles_de_propagation():
    '''Application des règles de propagation'''
    global fini 
    global terrain
    global copie_de_terrain

    copie_de_terrain = [[terrain[l][c] for c in range(N)] for l in range(N)]
    fini = True
    for l in range(N):
        for c in range(N):
            if t(l,c) == BRULE:
                terrain[l][c] = BRAISE
                fini = False
            if t(l,c) == BRAISE:
                terrain[l][c] = CENDRE
                fini = False
            if t(l,c) == ARBRE and au_moins_un_voisin_en_feu(l,c):
                terrain[l][c] = BRULE
                fini = False
            if t(l,c) == CYPRES and au_moins_un_voisin_en_feu(l,c):
                terrain[l][c] = CYPRES2
                fini = False
            if t(l,c) == CYPRES2:
                terrain[l][c] = BRULE
                fini = False
            if t(l,c) == FOUDRE:
                terrain[l][c] = FOUDRE2
                fini = False
            if t(l,c) == FOUDRE2:
                terrain[l][c] = FOUDRE3
                fini = False
            if t(l,c) == FOUDRE3:
                terrain[l][c] = BRULE
                fini = False      

def quadrillage():## réalisation du quadrillage... déjà vue !
    stroke(0)
    dx = width/(N)     
    dy = height/(N)    
    for i in range(1,N+1):
        line(i*dx,0, i*dx,height)
        line(0,i*dy, width, i*dy)
        
def affiche_le_terrain():
    dx = width/(N)     
    dy = height/(N)    
    for i in range(N):
        for j in range(N):
            if terrain[i][j] == VIDE:
                fill(135,89,26)
            elif terrain[i][j] == ARBRE:
                fill(0,255,0)
            elif terrain[i][j] == BRULE:
                fill(255,0,0)
            elif terrain[i][j] == CYPRES:
                fill(199,234,70)
            elif terrain[i][j] == BRAISE:
                fill(160,60,60)
            elif terrain[i][j] == CYPRES2:
                fill(208,240,192)
            elif terrain[i][j] == FOUDRE:
                fill(44,117,255)
            elif terrain[i][j] == FOUDRE2:
                fill(44,117,255)
            elif terrain[i][j] == FOUDRE3:
                fill(44,117,255)
            else:
                fill(175)
            rect(j*dx, i*dy, dx, dy)

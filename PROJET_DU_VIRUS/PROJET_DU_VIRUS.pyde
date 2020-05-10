######################################################
###    Simulation de la propagation d'un virus     ###
############################ NSI 2019 - 2020 #########

from random import *

#### déclaration des variables "globales" ####
N      = 50   # taille du tableau carré
SAIN  = 1
PORTEUR_SAIN  = 2
EN_INCUBATION = 3
MALADE = 4
MORT = 5
IMMUNISE = 6
taux_contamination = 0.4
taux_porteur_sains = 0.05
mortalite = 0.02
taux_immunise = 0.01

fini   = False 
terrain = [[SAIN for c in range(N)] for l in range(N)]
copie_de_terrain = [[SAIN for c in range(N)] for l in range(N)]



def setup(): # Au lancement du programme...
    size(600, 600)   # on crée une fenêtre 800x800
    rectMode(CORNER) # on sera en mode CORNER pour les rectangles
    frameRate(5)    # la boucle draw() sera appelée x fois par secondes
    population_immu() # on se fabrique une jolie forêt
    fallout(1)    # ...et on y allume plusieurs foyers
    
c = 0    
def draw():  # boucle draw(): 10 fois par secondes...
    background(255)                  # on efface l'écran et on le passe en fond blanc
    stroke(0)                        # tracé des traits en noir
    fill(255)                        # remplissage en blanc
    rect(0,0,width-1,height-1)       # on trace un rectangle sur le contour de l'écran
    quadrillage()                    # on réalise le quadrillage  
    affiche_le_terrain()             # on affiche le terrain
    applique_regles_de_propagation() # on applique les règles de propagation
 


def population_immu():
    '''peuplement du tableau 'terrain' avec une certaine densité d'arbres'''
    global terrain  # pour pouvoir modifier cette variable
    for ligne in range(N):
        for colonne in range(N):
            if random()<=taux_immunise: # si un nombre tiré au hasard est plus petit que "le taux d'immunisé" on suppose qu'on est bon
                terrain[ligne][colonne]=IMMUNISE # donc on pose une case immunisé
            else: #sinon
                terrain[ligne][colonne]=SAIN # sinon la case sera sain
            # ça fait le job car avec cette méthode, le taux d'immunisé =1 met toutes les cases à SAIN et le taux d'immunisé =0 aucune.

def fallout(nombre_de_contaminer):
    '''Allumage d'un certain nombre de porteur sain'''
    for i in range(nombre_de_contaminer):
        ligne = randint(0, N-1)
        colonne = randint(0, N-1)
        terrain[ligne][colonne] = PORTEUR_SAIN

def t(ligne, colonne):
    '''Fonction sentinelle qui vaut le contenu de copie_de_terrain si les coordonnées sont valides et SAIN sinon'''
    if (ligne<0) or (colonne<0) or (ligne>=N) or (colonne >= N) :
        return SAIN
    else :
        return copie_de_terrain[ligne][colonne]
  

def au_moins_un_voisin_malade(ligne,colonne):
    '''envoie True si au moins un des voisins de la case ligne,colonne est en feu'''
    if t(ligne-1,colonne-1)==MALADE or t(ligne-1,colonne)==MALADE or t(ligne-1,colonne+1)==MALADE or t(ligne,colonne-1)==MALADE or t(ligne,colonne+1)==MALADE or t(ligne+1,colonne-1)==MALADE or t(ligne+1,colonne)==MALADE or t(ligne+1,colonne+1)==MALADE :
        return True
    elif t(ligne-1,colonne-1)==PORTEUR_SAIN or t(ligne-1,colonne)==PORTEUR_SAIN or t(ligne-1,colonne+1)==PORTEUR_SAIN or t(ligne,colonne-1)==PORTEUR_SAIN or t(ligne,colonne+1)==PORTEUR_SAIN or t(ligne+1,colonne-1)==PORTEUR_SAIN or t(ligne+1,colonne)==PORTEUR_SAIN or t(ligne+1,colonne+1)==PORTEUR_SAIN :
        return True
    elif t(ligne-1,colonne-1)==EN_INCUBATION or t(ligne-1,colonne)==EN_INCUBATION or t(ligne-1,colonne+1)==EN_INCUBATION or t(ligne,colonne-1)==EN_INCUBATION or t(ligne,colonne+1)==EN_INCUBATION or t(ligne+1,colonne-1)==EN_INCUBATION or t(ligne+1,colonne)==EN_INCUBATION or t(ligne+1,colonne+1)==EN_INCUBATION :
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
            if t(l,c) == MALADE:
                if random()<=mortalite:
                    terrain[l][c] = MORT
                else:
                    terrain[l][c] = IMMUNISE
                    fini = False
            if t(l,c) == EN_INCUBATION:   
                terrain[l][c] = MALADE
                fini = False      
            
            if t(l,c) == SAIN and au_moins_un_voisin_malade(l,c):
                if random()<=taux_contamination:
                    terrain[l][c] = EN_INCUBATION
                elif random()<=taux_porteur_sains: 
                    terrain[l][c] = PORTEUR_SAIN
                else:
                    terrain[l][c] = SAIN         

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
            if terrain[i][j] == PORTEUR_SAIN:
                fill(255,255,0)
            elif terrain[i][j] == EN_INCUBATION:
                fill(255,165,0)
            elif terrain[i][j] == MALADE:
                fill(255,0,0)    
            elif terrain[i][j] == MORT:
                fill(211,211,211)
            elif terrain[i][j] == IMMUNISE:
                fill(0,100,0)
            else:
                fill(0,255,0)
            rect(j*dx, i*dy, dx, dy)

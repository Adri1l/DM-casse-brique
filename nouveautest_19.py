# on rajoute random
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 55
vaisseau_y = 110

#bloc 1e ligne
bloc_x = 0
bloc_x2 = 10
bloc_x3 = 20
bloc_x4 = 30
bloc_x5 = 40
bloc_x6 = 50
bloc_x7 = 60
bloc_x8 = 70
bloc_x9 = 80
bloc_x10 = 90
bloc_x11 = 100
bloc_x12 = 110
bloc_x13 = 120


bloc_y = 0

#bloc 2e ligne
bloc_x14 = 0
bloc_x15 = 10
bloc_x16 = 20
bloc_x17 = 30
bloc_x18 = 40
bloc_x19 = 50
bloc_x20 = 60
bloc_x21 = 70
bloc_x22 = 80
bloc_x23 = 90
bloc_x24 = 100
bloc_x25 = 110
bloc_x26 = 120


bloc_y2 = 10

# initialisation des tirs
tirs_liste = []

# initialisation des ennemis
ennemis_liste = []


def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 3
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 3

    return x, y


def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""

    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+12, y-4])
    return tirs_liste


def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 4
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste

def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste


def ennemis_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)

    # creation des ennemis
    ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 25, 8, 1)
    pyxel.tri(vaisseau_x +24, vaisseau_y, vaisseau_x +24, vaisseau_y + 7, vaisseau_x +24 + 7, vaisseau_y + 7,1)
    pyxel.tri(vaisseau_x , vaisseau_y, vaisseau_x , vaisseau_y + 7, vaisseau_x -7, vaisseau_y + 8,1)

    # tirs
    for tir in tirs_liste:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)

    # ennemis 1e ligne
    pyxel.rect(bloc_x, bloc_y, 8, 8, 4)   
    pyxel.rect(bloc_x2, bloc_y, 8, 8, 4)  
    pyxel.rect(bloc_x3, bloc_y, 8, 8, 4)    
    pyxel.rect(bloc_x4, bloc_y, 8, 8, 4)  
    pyxel.rect(bloc_x5, bloc_y, 8, 8, 4)   
    pyxel.rect(bloc_x6, bloc_y, 8, 8, 4)  
    pyxel.rect(bloc_x7, bloc_y, 8, 8, 4)   
    pyxel.rect(bloc_x8, bloc_y, 8, 8, 4)  
    pyxel.rect(bloc_x9, bloc_y, 8, 8, 4)   
    pyxel.rect(bloc_x10, bloc_y, 8, 8, 4)  
    pyxel.rect(bloc_x11, bloc_y, 8, 8, 4)   
    pyxel.rect(bloc_x12, bloc_y, 8, 8, 4)  
    pyxel.rect(bloc_x13, bloc_y, 8, 8, 4)   

    # ennemis 2e ligne

    pyxel.rect(bloc_x14, bloc_y2, 8, 8, 4)   
    pyxel.rect(bloc_x15, bloc_y2, 8, 8, 4)  
    pyxel.rect(bloc_x16, bloc_y2, 8, 8, 4)    
    pyxel.rect(bloc_x17, bloc_y2, 8, 8, 4)  
    pyxel.rect(bloc_x18, bloc_y2, 8, 8, 4)   
    pyxel.rect(bloc_x19, bloc_y2, 8, 8, 4)  
    pyxel.rect(bloc_x20, bloc_y2, 8, 8, 4)   
    pyxel.rect(bloc_x21, bloc_y2, 8, 8, 4)  
    pyxel.rect(bloc_x22, bloc_y2, 8, 8, 4)   
    pyxel.rect(bloc_x23, bloc_y2, 8, 8, 4)  
    pyxel.rect(bloc_x24, bloc_y2, 8, 8, 4)   
    pyxel.rect(bloc_x25, bloc_y2, 8, 8, 4)  
    pyxel.rect(bloc_x26, bloc_y2, 8, 8, 4)   



pyxel.run(update, draw)

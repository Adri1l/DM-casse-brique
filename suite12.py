import pyxel, random


pyxel.init(256, 256, title="DM_NSI_CASSEBRIQUE")


balle_x = 128
balle_y = 128
vaisseau_x = 120
vaisseau_y = 200
deplacement_vertical = 3
deplacement_horizontal = random.randint(-1,5)
vies = 5
vies_brique_1 = 1


def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 270-32-14-2) :
            x = x + 4
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 8) :
            x = x - 4
    return x, y

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_y, balle_x, deplacement_vertical, deplacement_horizontal, vies


    vaisseau_x, vaisseau_y = plateau_deplacement(vaisseau_x, vaisseau_y)

    balle_y = balle_y + deplacement_vertical 
    balle_x = balle_x + deplacement_horizontal 
    deplacement_vertical = deplacement_vertical 
    deplacement_horizontal = deplacement_horizontal 

    if balle_x >= 256 : 
        deplacement_horizontal =-3 #-1


    if balle_x <= 0 : 
        deplacement_horizontal = 2  #1 

    if balle_y >= 230 :
        vies = vies - 1
        balle_y = 110
        balle_x = 128
        deplacement_horizontal = random.randint(-1,1)


    if balle_y <= 0 :
        deplacement_vertical = 1 #1

    if vaisseau_y <= balle_y <= vaisseau_y + 20 and vaisseau_x <= balle_x <=vaisseau_x + 25 :
        deplacement_vertical = -3 #-1


    if vaisseau_y <= balle_y <= vaisseau_y + 20  and vaisseau_x + 25 <= balle_x <=vaisseau_x + 25 + 16 :
        deplacement_vertical = -3 #-1
        #deplacement_horizontal = -1 #1
        if deplacement_horizontal == -2 or deplacement_horizontal == 0 :
            deplacement_horizontal = 1 #-1  
        if deplacement_horizontal == 1 :
            deplacement_horizontal == 1

    if vaisseau_y <= balle_y <= vaisseau_y + 20 and vaisseau_x - 25 <= balle_x <= vaisseau_x :
        deplacement_vertical = -1 #-1
        if deplacement_horizontal == 1 or deplacement_horizontal == 0 :
            deplacement_horizontal = -1 #-1  
        if deplacement_horizontal == -1 :
            deplacement_horizontal == 1

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_y, balle_x, deplacement_vertical, vies, vies_brique_1, deplacement_horizontal

    if vies > 0 :
    # vide la fenetre
        pyxel.cls(0)


    # plateau 
        pyxel.rect(vaisseau_x, vaisseau_y, 25, 8, 9)
        pyxel.tri(vaisseau_x + 24, vaisseau_y, vaisseau_x + 24, vaisseau_y + 7, vaisseau_x + 24 + 7, vaisseau_y + 7, 9)
        pyxel.tri(vaisseau_x , vaisseau_y, vaisseau_x , vaisseau_y + 7, vaisseau_x - 7, vaisseau_y + 7, 9)

    #balle 
        pyxel.circ(balle_x, balle_y, 6, 9)

        if balle_y == 25 and 128-13 <= balle_x <= 128-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_vertical = -1 #-1

        elif balle_y == 25+17 and 128-13 < balle_x < 128-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_vertical = 1 #1

    #lave
          pyxel.rect(0, 130, 256, 100, 8)

        #affichage brique

        if vies_brique_1 > 0 :
            pyxel.rect(128-13, 25, 25, 17, 9)


    #fin
    if vies == 0 :
        pyxel.cls(0)
        pyxel.text(120,128,"PERDU", 9)

    if vies_brique_1 == 0 :
        pyxel.cls(0)
        pyxel.text(100,115,"BRAVO C'EST GAGNE ! ! !",9)
""



pyxel.run(update, draw)
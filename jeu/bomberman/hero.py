import pygame

class Hero :

    def __init__(self):
        self.x = 50
        self.y = 50
        self.largeur = 50
        self.hauteur = 50
        self.couleur = (255 , 0 , 0)

    
    def dessiner(self, screen) :   
        pygame.draw.rect(screen,
            self.couleur , 
            (self.x, self.y, self.largeur, self.hauteur))
        
    def deplacement_bas(self) :
        self.y += 10

    def deplacement_haut(self) :
        self.y -= 10

    def deplacement_droite(self) :
        self.x += 10

    def deplacement_gauche(self) :
        self.x -= 10
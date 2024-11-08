import pygame

class Obstacle :

    def __init__(self):
        self.x = 100
        self.y = 100
        self.largeur = 50
        self.hauteur = 50
        self.couleur = (0 , 255 , 0)

    def dessiner(self, screen) :   
        pygame.draw.rect(screen,
            self.couleur , 
            (self.x, self.y, self.largeur, self.hauteur))
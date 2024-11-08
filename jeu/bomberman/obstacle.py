import pygame

class Obstacle :

    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.largeur = 50
        self.hauteur = 50
        self.couleur = (0 , 255 , 0)
        self.hitbox = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)


    def dessiner(self, screen) :   
        pygame.draw.rect(screen,
            self.couleur , 
            (self.x, self.y, self.largeur, self.hauteur))
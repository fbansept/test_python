import pygame

from config import Config

class Hero :

    def __init__(self):
        self.x = 50
        self.y = 50
        self.largeur = 50
        self.hauteur = 50
        self.couleur = (255 , 0 , 0)


    def deplacement(self) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.deplacement_droite()
        if keys[pygame.K_LEFT]:
            self.deplacement_gauche()
        if keys[pygame.K_UP]:
            self.deplacement_haut()
        if keys[pygame.K_DOWN]:
            self.deplacement_bas()

    
    def dessiner(self, screen) :   
        pygame.draw.rect(screen,
            self.couleur , 
            (self.x, self.y, self.largeur, self.hauteur))
        
    def deplacement_bas(self) :
        if self.y < Config.screen_height - self.hauteur:
            self.y += 10

    def deplacement_haut(self) :
        if self.y > 0:
            self.y -= 10

    def deplacement_droite(self) :
        if self.x < Config.screen_width - self.largeur:
            self.x += 10

    def deplacement_gauche(self) :
        if self.x > 0:
            self.x -= 10
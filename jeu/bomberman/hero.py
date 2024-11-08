import pygame

from config import Config

class Hero :

    def __init__(self):
        self.x = 50
        self.y = 50
        self.largeur = 50
        self.hauteur = 50
        self.couleur = (255 , 0 , 0)


    def deplacement(self, obstacle) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.deplacement_droite(obstacle)
        if keys[pygame.K_LEFT]:
            self.deplacement_gauche(obstacle)
        if keys[pygame.K_UP]:
            self.deplacement_haut(obstacle)
        if keys[pygame.K_DOWN]:
            self.deplacement_bas(obstacle)

    
    def dessiner(self, screen) :   
        pygame.draw.rect(screen,
            self.couleur , 
            (self.x, self.y, self.largeur, self.hauteur))
        
    def deplacement_bas(self, obstacle) :
        if self.y < Config.screen_height - self.hauteur:
            self.y += 10

    def deplacement_haut(self, obstacle) :
        if self.y > 0:
            self.y -= 10

    def deplacement_droite(self, obstacle) :
        if self.x < Config.screen_width - self.largeur:
            self.x += 10

    def deplacement_gauche(self, obstacle) :
        if self.x > 0:
            self.x -= 10
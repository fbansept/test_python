import pygame
import random

class Balle :

    def __init__(self, screen_width, screen_height):
        self.rayon = random.randint(5,30)
        self.x = random.randint(self.rayon, screen_width - self.rayon)
        self.y = random.randint(self.rayon, screen_height - self.rayon)
        self.vitesse_x = random.randint(1,10)
        self.vitesse_y = random.randint(1,10)
        self.couleur = (random.randint(0,220),
                        random.randint(0,220),
                        random.randint(0,220))

    def dessiner(self, screen) :
        pygame.draw.circle(screen,
                            self.couleur , 
                            (self.x, self.y), 
                            self.rayon)
        
    def deplacement(self, screen_width, screen_height) :
        self.x += self.vitesse_x
        self.y += self.vitesse_y

        if self.x + self.rayon >= screen_width or self.x  <= self.rayon:
            self.vitesse_x = -self.vitesse_x

        if self.y + self.rayon >= screen_height or self.y <= self.rayon:
            self.vitesse_y = -self.vitesse_y
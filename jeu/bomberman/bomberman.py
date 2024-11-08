import pygame
import sys
from config import Config
from hero import Hero
from obstacle import Obstacle

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre

screen = pygame.display.set_mode((Config.screen_width, Config.screen_height))
pygame.display.set_caption("Bomberman")

en_cours = True
clock = pygame.time.Clock()


  # créer une classe hero
  # # x y largeur hauteur
  # créer un objet hero <--------------

hero = Hero()
obstacle = Obstacle()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False


    # Remplir l'écran 
    screen.fill((255,255,255))

    #dessiner le hero <--------------
    hero.dessiner(screen)
    hero.deplacement()
    
    obstacle.dessiner(screen)

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter pygame
pygame.quit()
sys.exit()
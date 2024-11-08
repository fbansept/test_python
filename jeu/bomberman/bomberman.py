import pygame
import sys
from hero import Hero

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bomberman")

en_cours = True
clock = pygame.time.Clock()


  # créer une classe hero
  # # x y largeur hauteur
  # créer un objet hero <--------------

hero = Hero()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :
                hero.deplacement_bas()
            elif event.key == pygame.K_UP :
                hero.deplacement_haut()
            elif event.key == pygame.K_RIGHT :
                hero.deplacement_droite()
            elif event.key == pygame.K_LEFT :
                hero.deplacement_gauche()

    # Remplir l'écran 
    screen.fill((255,255,255))

    #dessiner le hero <--------------
    hero.dessiner(screen)


    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter pygame
pygame.quit()
sys.exit()
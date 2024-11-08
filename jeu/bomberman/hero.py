import pygame

from config import Config

class Hero :

    def __init__(self):
        self.x = 50
        self.y = 50
        self.largeur = 50
        self.hauteur = 50
        self.couleur = (255 , 0 , 0)
        self.rectHero = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)


    def deplacement(self, liste_obstacles) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.deplacement_droite(liste_obstacles)
        if keys[pygame.K_LEFT]:
            self.deplacement_gauche(liste_obstacles)
        if keys[pygame.K_UP]:
            self.deplacement_haut(liste_obstacles)
        if keys[pygame.K_DOWN]:
            self.deplacement_bas(liste_obstacles)

    
    def dessiner(self, screen) :   
        pygame.draw.rect(screen,
            self.couleur , 
            (self.x, self.y, self.largeur, self.hauteur))
        
    def deplacement_bas(self, liste_obstacles) :

        prevision_hitbox_hero = pygame.Rect(self.x , self.y + 10, self.largeur, self.hauteur)

        #on test si une collision se produirait dans le cas d'un déplacement vers le bas
        prevision_collision = False

        for obstacle in liste_obstacles :
            if prevision_hitbox_hero.colliderect(obstacle.hitbox):
                prevision_collision = True
                break

        if not prevision_collision and self.y < Config.screen_height - self.hauteur:
            self.y += 10

    def deplacement_haut(self, liste_obstacles) :

        prevision_hitbox_hero = pygame.Rect(self.x , self.y - 10, self.largeur, self.hauteur)

        #on test si une collision se produirait dans le cas d'un déplacement vers le bas
        prevision_collision = False

        for obstacle in liste_obstacles :
            if prevision_hitbox_hero.colliderect(obstacle.hitbox):
                prevision_collision = True
                break

        if not prevision_collision and self.y > 0:
            self.y -= 10

    def deplacement_droite(self, liste_obstacles) :

        prevision_hitbox_hero = pygame.Rect(self.x + 10, self.y, self.largeur, self.hauteur)

        #on test si une collision se produirait dans le cas d'un déplacement vers le bas
        prevision_collision = False

        for obstacle in liste_obstacles :
            if prevision_hitbox_hero.colliderect(obstacle.hitbox):
                prevision_collision = True
                break

        if not prevision_collision and self.x < Config.screen_width - self.largeur:
            self.x += 10

    def deplacement_gauche(self, liste_obstacles) :

        prevision_hitbox_hero = pygame.Rect(self.x - 10, self.y, self.largeur, self.hauteur)
        
        #on test si une collision se produirait dans le cas d'un déplacement vers le bas
        prevision_collision = False

        for obstacle in liste_obstacles :
            if prevision_hitbox_hero.colliderect(obstacle.hitbox):
                prevision_collision = True
                break

        if not prevision_collision and self.x > 0:
            self.x -= 10
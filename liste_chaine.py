class Element :
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None


class Liste :
    def __init__(self):
        self.premier_element = None
        self.dernier_element = None

    def ajout(self, valeur_element) :
        nouvel_element = Element(valeur_element)

        if self.premier_element == None :
            self.premier_element = nouvel_element
        else : 
            self.dernier_element.suivant = nouvel_element

        self.dernier_element = nouvel_element

    def afficher_tout(self) :

        element_actuel = self.premier_element
        
        while element_actuel != None :
            print(element_actuel.valeur)
            element_actuel = element_actuel.suivant
        
    def supprimer_dernier(self) :
        element_actuel = self.premier_element
        
        while element_actuel.suivant != self.dernier_element :
            element_actuel = element_actuel.suivant

        element_actuel.suivant = None
        self.dernier_element = element_actuel

    def supprimer_element(self, index_element_a_supprimer) :

        element_actuel = self.premier_element
        compteur = 0
        
        while compteur != index_element_a_supprimer - 1 :
            element_actuel = element_actuel.suivant
            compteur += 1

        element_actuel.suivant = element_actuel.suivant.suivant

        
    def donne_inverse(self) :

        liste_inverse = Liste()

        element_actuel = self.premier_element

        while element_actuel != None :

            liste_inverse.ajout_debut(element_actuel.valeur)

            #on passe a l'élément suivant de la liste d'origine
            element_actuel = element_actuel.suivant

        return liste_inverse
    
    #--- exo 3 ----
    def inverse(self):
        """Méthode qui inverse les éléments de la liste elle-même"""
        element_precedent = None
        element_actuel = self.premier_element
        self.dernier_element = self.premier_element  # Le premier élément deviendra le dernier après inversion

        while element_actuel is not None:
            element_suivant = element_actuel.suivant   # Sauvegarde l'élément suivant avant de changer le lien

            element_actuel.suivant = element_precedent

            element_precedent = element_actuel
            element_actuel = element_suivant

        self.premier_element = element_precedent


        

    def afficher_tout_inverse(self) :

        #---- solution 1-----
        liste_inversee = ma_liste.donne_inverse()
        liste_inversee.afficher_tout()

        #---- solution 2 (un peu triché) -----
        # affichage = ""

        # element_actuel = self.premier_element
        
        # while element_actuel != None :
        #     affichage = element_actuel.valeur + "\n" + affichage
        #     element_actuel = element_actuel.suivant

        # print(affichage)

    
    def ajout_debut(self, valeur_element) :

        #on créait une copie de l'élément
        nouvel_element = Element(valeur_element)

        if self.dernier_element == None :
            self.dernier_element = nouvel_element

        #la copie aura pour suivant le premier element
        nouvel_element.suivant = self.premier_element

        #la copie devient le premier element
        self.premier_element = nouvel_element


ma_liste = Liste()

ma_liste.ajout("A")
ma_liste.ajout("B")
ma_liste.ajout("C")
ma_liste.ajout("D")

ma_liste.inverse()

ma_liste.afficher_tout()

verreA = "rouge"
verreB = "bleu"
verreC = verreA
verreA = verreB
verreB = verreC



# for avec different arguments

# priorité sur les booléens

#
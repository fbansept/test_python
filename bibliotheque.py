class Livre :
    
    def __init__(self, titre, auteur, annee_de_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_de_publication = annee_de_publication
        self.disponible = True

    def afficher_info(self) :
        print(f'"{self.titre}" de {self.auteur} ({self.annee_de_publication}) est {"disponible" if self.disponible else "indisponible"}')
        
    def emprunter(self) :
        if self.disponible :
            self.disponible = False
        else :
            print("Le livre est indisponible")

    def retourner(self) :
        self.disponible = True


class LivreNumerique(Livre) :

    def __init__(self, titre, auteur, annee_de_publication, format_fichier):
        super().__init__(titre, auteur, annee_de_publication)
        self.format_fichier = format_fichier

    def emprunter(self) :
        pass

    def afficher_info(self) :
        print(f'{self.titre}-{self.auteur}.{self.format_fichier} est {"disponible" if self.disponible else "indisponible"}')
        

class Magazine(Livre) :

    def __init__(self, titre, auteur, annee_de_publication, numero):
        super().__init__(titre, auteur, annee_de_publication)
        self.numero = numero

    def afficher_info(self) :
        print(f'"{self.titre}" numero {self.numero} de {self.auteur} ({self.annee_de_publication}) est {"disponible" if self.disponible else "indisponible"}')


class Bibliotheque :

    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre) :
        self.livres.append(livre)

    def afficher_tous_les_livres(self) :
        for livre in self.livres :
            livre.afficher_info()

    def compter_livres_disponibles(self) :

        compteur = 0

        for livre in self.livres :
            if livre.disponible :
                compteur += 1  

        return compteur
    
    def recherche_livres(self, recherche) :

        resultat = []

        for livre in self.livres :
            if  recherche in livre.titre or recherche in livre.auteur:
                resultat.append(livre)
            
        return resultat



picsou_magazine = Magazine("Pissou","Disney",1990,42)
livre_les_miserable = Livre("Les Misérables", "Victor Hugo", 1862)
livre_1984 = LivreNumerique("1984", "George Orwell", 1949, "PDF")
magazine_national_geo = Magazine("National Geographic", "Divers", 2024, 150)


ma_bibliotheque = Bibliotheque()
ma_bibliotheque.ajouter_livre(picsou_magazine)
ma_bibliotheque.ajouter_livre(livre_les_miserable)
ma_bibliotheque.ajouter_livre(livre_1984)
ma_bibliotheque.ajouter_livre(magazine_national_geo)

picsou_magazine.emprunter()
livre_1984.emprunter()
magazine_national_geo.emprunter()

for livre_trouve in ma_bibliotheque.recherche_livres("ic") :
    livre_trouve.afficher_info()



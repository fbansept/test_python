class Produit:

    def __init__(self, nom, prix_ht, tva, quantite) :
        self.nom = nom
        self.prix_ht = prix_ht
        self.tva = tva
        self.quantite = quantite

    def prix_ttc(self):
        return self.prix_ht * (self.tva / 100 + 1)
    
    def chiffre_affaire_ttc_possible(self):
        return self.prix_ttc() * self.quantite
    

class Magasin:

    def __init__(self, liste_produit = []):
        self.liste_produit = liste_produit

    def rupture_produit(self) :
        for prd in self.liste_produit :
            if prd.quantite <= 0:
                print(f"Le produit {prd.nom} est en rupture")

    def chiffre_affaire_ttc_en_stock(self):
        cumul = 0

        for prd in self.liste_produit :
            cumul += prd.chiffre_affaire_ttc_possible()

        return cumul
    
    def chiffre_affaire_selon_produit(self, nom_produit) :
        
        for prd in self.liste_produit :
            if prd.nom == nom_produit :
                return prd.chiffre_affaire_ttc_possible()
            
        return 0
    
    def changer_quantite_produit(self) :

        nom_produit = input("Saisissez le nom du produit à modifier")
        nouvelle_quantite_produit = input("Saisissez la quantite du produit à modifier")

        for prd in self.liste_produit :
            if prd.nom == nom_produit :
                prd.quantite = nouvelle_quantite_produit
                break



mon_magasin = Magasin()

choix = -1

while choix != 5 :
    print("Taper le numero de l'opération désirée :")
    print("1 = saisir un nouveau produit")
    print("2 = modifier sa quantité") 
    print("3 = lister les produits en rupture de stocke")
    print("4 = calculer le Chiffre d'affaire TTC réalisable avec le stock")
    print("5 = quitter le programme")

    choix = input("")

    if choix == 1 :

        nouveau_produit = Produit(
            input("Saisir le nom du produit"),
            float(input("Saisir le prix du produit")),
            float(input("Saisir la TVA du produit")),
            int(input("Saisir la quantite du produit")))
        
        mon_magasin.liste_produit.append(nouveau_produit)

    elif choix == 2 :

        mon_magasin.changer_quantite_produit()

    elif choix == 3 :
        
        mon_magasin.rupture_produit()   

    elif choix == 4 :
        
        mon_magasin.chiffre_affaire_ttc_en_stock()
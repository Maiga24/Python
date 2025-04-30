class Panier:
     
    def __init__(self):
        self.produits = {} 
        
    def ajouterProduit(self, nom, qte):
        self.produits[nom] =  qte
        print("succes!")
            
    def supprimerProduit(self, nom):
        if nom in self.produits:
            del self.produits[nom] 
            
    def affichePanier(self):
        for nom, qte in self.produits.items():
            print(f'{nom}: {qte}')  
            
p1 = Panier()

p1.ajouterProduit("cacao", 10) 
p1.ajouterProduit("banane", 10) 
print("=== Liste des produits du panier")
p1.affichePanier()
 
print("=== Apres suppression ")
p1.supprimerProduit("cacao")
p1.affichePanier() 


    
    
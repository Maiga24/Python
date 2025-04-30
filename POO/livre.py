class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.liste = [] 
    
    def __str__(self):
        return (f'{self.titre}, par {self.auteur} en {self.annee}')


    
 
liste = [
    Livre("Python Facile", "Salif S.", 2016),
    Livre("Java Débutant", "Toto Y.", 2012),
    Livre("Angular ", "Aïssata M.", 2014),
    Livre("IA", "Souleymane D.", 2015),
    Livre("Dev Web ", "Maïga A.", 2023)
]
        

for livre in liste:
    if(livre.annee > 2015):
        print(livre)
    
    

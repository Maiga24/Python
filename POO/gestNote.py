class Etudiant:
    def __init__(self, nom, prenom, notes):
        self.nom = nom
        self.prenom = prenom
        self.notes = notes

    def moyenne(self):
        return sum(self.notes) / len(self.notes)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} {self.notes}"
    
class Classe:
    def __init__(self):
        self.etudiants = []
        
    def ajouterEtudiant(self, etudiant):
        self.etudiants.append(etudiant)
        print("success")
        
    def afficherEtudiants(self):
        for etudiant in self.etudiants:
            print(etudiant) 
        
    def moyenne_generale(self):
        if not self.etudiants:
            return 0
        total = sum(etu.moyenne() for etu in self.etudiants)
        return total / len(self.etudiants)    
            
            
e1 = Etudiant("maiga", "aissa", [2,2,2,2])
e2 = Etudiant("fanta", "aissa", [2,2,2,2])
e3 = Etudiant("binta", "aissa", [2,2,2,2])


print(e1)
moy = e1.moyenne()
print(moy)

l1 = Classe()
l1.ajouterEtudiant(e1)
l1.ajouterEtudiant(e2)
l1.ajouterEtudiant(e3)

l1.afficherEtudiants()
moyenneGenerale = l1.moyenne_generale()
print(moyenneGenerale)

 

            
            
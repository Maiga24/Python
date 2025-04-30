class Etudiant:
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau
        self.notes = {}
        
    def ajouterNotes(self, matiere, note):
        self.notes[matiere] = note
        
    def afficherEtudiant(self):
        print(f"Pour l'etudiant {self.nom}  de la {self.niveau}")
        for matiere, note in self.notes.items():
            print(f"{matiere}: {note}")
            
maiga = Etudiant("Aïssata Maïga", "L4")
maiga.ajouterNotes("HTML", 15)
maiga.ajouterNotes("Angular", 16)
maiga.ajouterNotes("Spring", 14)
maiga.ajouterNotes("Algo", 18)

maiga.afficherEtudiant()
            
            
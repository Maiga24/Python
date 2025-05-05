import os
import json

# 2. Structures de Données à Utiliser

#### **Classe `Etudiant`**  

class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, date_naissance, classe):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.classe = classe
        
    def __str__(self):
        return f"{self.id_etudiant} {self.nom} {self.prenom} {self.date_naissance} {self.classe}"
    
    def dict_etudiant(self):
        return {
            "id_etudiant": self.id_etudiant,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "classe": self.classe
        }
        
    
class GestionEtudiant:
    def __init__(self, fichier = "etudiants.json"):
        self.fichier = fichier
        self.etudiants = self.charger()
        
    def charger(self):
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, 'r') as f:
                    data = json.load(f)
                    return [Etudiant(**e) for e in data]
            except (json.JSONDecodeError, TypeError):
                print("Fichier JSON vide ou corrompu. Initialisation d'une liste vide.")
                return []
        return []

        
    def sauvegarder(self):
        with open(self.fichier, 'w') as f:
            json.dump([e.dict_etudiant() for e in self.etudiants], f, indent=4)
            
    def ajouter_etudiant(self, etudiant):
        if any(e.id_etudiant == etudiant.id_etudiant for e in self.etudiants):
            print("Un etudiant ave det ID existe déjà !")
            return
        self.etudiants.append(etudiant)
        self.sauvegarder()
        print("Etudiant ajouté avec succes")
        
    def supprimer_etudiant(self, id_etudiant):
        for e in self.etudiants:
            if(e.id_etudiant == id_etudiant):
                self.etudiants.remove(e)
                self.sauvegarder()
                print("Etudiant supprimer avec succes")
                
            print("Etudiant introuvable")
            
    def afficher_etudiants(self):
        if not self.etudiants:
            print("Aucun etudiant en registré")
        for e in self.etudiants:
            print(f"{e.id_etudiant} | {e.nom} {e.prenom} | {e.date_naissance} | Classe: {e.classe}")
   
    def modifier_etudiant(self, id_etudiant, **kwargs):
        for e in self.etudiants:
            if e.id_etudiant == id_etudiant:
                e.nom = kwargs.get('nom', e.nom)
                e.prenom = kwargs.get('prenom', e.prenom)
                e.date_naissance = kwargs.get('date_naissance', e.date_naissance)
                e.classe = kwargs.get('classe', e.classe)
                self.sauvegarder()
                print("Etudiant modifié.")
                return
        print("Etudiant introuvable.")
         
        
            
        
#### **Classe `Matiere`** 
 
class Matiere:
    def __init__(self, code_matiere, nom_matiere, coefficient):
        self.code_matiere = code_matiere
        self.nom_matiere = nom_matiere
        self.coefficient = coefficient
        
    def dict_matiere(self):
        return{
            "code_matiere": self.code_matiere,
            "nom_matiere": self.nom_matiere,
             "coefficient": self.coefficient  
        }
        
    def __str__(self):
        return f"{self.code_matiere} {self.nom_matiere} {self.coefficient}"
    
class GestionMatiere:
    def __init__(self, fichier = "matiere.json"):
        self.fichier = fichier
        self.matieres = self.charger()
        
    def charger(self):
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, 'r') as f:
                    data = json.load(f)
                    return [Matiere(**e) for e in data]
            except (json.JSONDecodeError, TypeError):
                print("Fichier JSON vide")
                return []
        return []
    
    def afficher_matieres(self):
        if not self.matieres:
            print("Aucune matiere enregistrée")
        for e in self.matieres:
            print(f"{e.code_matiere} | Matiere: {e.nom_matiere}| Coefficient: {e.coefficient}")


        
    def sauvegarder(self):
        with open(self.fichier, 'w') as f:
            json.dump([e.dict_matiere() for e in self.matieres], f, indent=4)
            
    def ajouter_matiere(self, matiere):
        if any(e.code_matiere == matiere.code_matiere for e in self.matieres):
            print("Une matiere avec cet ID existe déjà !")
            return
        self.matieres.append(matiere)
        self.sauvegarder()
        print("Matiere ajouté avec succes")


#### **Classe `Note`**  
  
class Note:
    def __init__(self, id_etudiant, code_matiere, valeur_note, date_evaluation):
        self.id_etudiant = id_etudiant
        self.code_matiere = code_matiere
        self.valeur_note = valeur_note
        self.date_evaluation = date_evaluation
        
    def __str__(self):
        return f"{self.id_etudiant} {self.code_matiere} {self.valeur_note} {self.date_evaluation}"


class GestionNote:
    def __init__(self, fichier="notes.json"):
        self.fichier = fichier
        self.notes = self.charger()

    def charger(self):
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, 'r') as f:
                    data = json.load(f)
                    return [Note(**n) for n in data]
            except (json.JSONDecodeError, TypeError):
                print("Fichier de notes vide ou corrompu. Initialisation vide.")
                return []
        return []

    def sauvegarder(self):
        with open(self.fichier, 'w') as f:
            json.dump([note.__dict__ for note in self.notes], f, indent=4)

    def saisir_note(self, note):
        for n in self.notes:
            if (n.id_etudiant == note.id_etudiant and 
                n.code_matiere == note.code_matiere and 
                n.date_evaluation == note.date_evaluation):
                print("Note déjà enregistrée pour cet étudiant dans cette matière ")
                return
        self.notes.append(note)
        self.sauvegarder()
        print("Note saisie avec succès.")

    def modifier_note(self, id_etudiant, code_matiere, date_evaluation, nouvelle_valeur):
        for note in self.notes:
            if (note.id_etudiant == id_etudiant and 
                note.code_matiere == code_matiere and 
                note.date_evaluation == date_evaluation):
                note.valeur_note = nouvelle_valeur
                self.sauvegarder()
                print("Note modifiée avec succès.")
                return
        print("Note introuvable.")

    def afficher_notes(self):
        if not self.notes:
            print("Aucune note enregistrée.")
            return
        for note in self.notes:
            print(f"Etudiant ID: {note.id_etudiant} | Matière: {note.code_matiere} | Note: {note.valeur_note} | Date: {note.date_evaluation}")

    
    
    def calculer_moyenne_matiere(self, id_etudiant, code_matiere):
        notes_matiere = [n for n in self.notes if n.id_etudiant == id_etudiant and n.code_matiere == code_matiere]
        if not notes_matiere:
            return None
        total = sum(n.valeur_note for n in notes_matiere)
        return round(total / len(notes_matiere), 2)

    def calculer_moyenne_generale(self, id_etudiant, gestion_matiere):
        matieres_codes = list({n.code_matiere for n in self.notes if n.id_etudiant == id_etudiant})
        total_points = 0
        total_coeff = 0
        for code in matieres_codes:
            moyenne = self.calculer_moyenne_matiere(id_etudiant, code)
            coeff = next((m.coefficient for m in gestion_matiere.matieres if m.code_matiere == code), 1)
            if moyenne is not None:
                total_points += moyenne * coeff
                total_coeff += coeff
        if total_coeff == 0:
            return None
        return round(total_points / total_coeff, 2)

    def afficher_bulletin(self, id_etudiant, gestion_matiere, gestion_etudiant):
        etudiant = next((e for e in gestion_etudiant.etudiants if e.id_etudiant == id_etudiant), None)
        if not etudiant:
            print("Étudiant introuvable.")
            return
        print(f"\n--- Bulletin de {etudiant.nom} {etudiant.prenom} ---\n")
        print(f"Classe : {etudiant.classe}")
        print(f"Date de naissance : {etudiant.date_naissance}\n")

        notes_par_matiere = {}
        for note in self.notes:
            if note.id_etudiant == id_etudiant:
                notes_par_matiere.setdefault(note.code_matiere, []).append(note)

        for code_matiere, notes in notes_par_matiere.items():
            nom_matiere = next((m.nom_matiere for m in gestion_matiere.matieres if m.code_matiere == code_matiere), code_matiere)
            print(f"--- {nom_matiere} ---")
            for note in notes:
                print(f"Note: {note.valeur_note} | Date: {note.date_evaluation}")
            moyenne = self.calculer_moyenne_matiere(id_etudiant, code_matiere)
            print(f"Moyenne dans la matière: {moyenne}\n")

        moyenne_gen = self.calculer_moyenne_generale(id_etudiant, gestion_matiere)
        print(f"*** Moyenne Générale : {moyenne_gen} ***\n")
        
        


def menu_principal():
    gestion_etudiant = GestionEtudiant()
    gestion_matiere = GestionMatiere()
    gestion_note = GestionNote()

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gestion des étudiants")
        print("2. Gestion des matières")
        print("3. Saisie des notes")
        print("4. Calcul des moyennes")
        print("5. Affichage des bulletins")
        print("6. Sauvegarder les données")
        print("7. Charger les données")
        print("8. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            print("\n-- Gestion des étudiants --")
            print("1. Ajouter étudiant")
            print("2. Supprimer étudiant")
            print("3. Modifier étudiant")
            print("4. Afficher les étudiants")
            sous_choix = input("Choix : ")
            if sous_choix == "1":
                id_ = input("ID : ")
                nom = input("Nom : ")
                prenom = input("Prénom : ")
                date_naiss = input("Date de naissance : ")
                classe = input("Classe : ")
                etu = Etudiant(id_, nom, prenom, date_naiss, classe)
                gestion_etudiant.ajouter_etudiant(etu)
            elif sous_choix == "2":
                id_ = input("ID de l'étudiant à supprimer : ")
                gestion_etudiant.supprimer_etudiant(id_)
            elif sous_choix == "3":
                id_ = input("ID de l'étudiant à modifier : ")
                nom = input("Nouveau nom (laisser vide pour garder l'ancien) : ")
                prenom = input("Nouveau prénom : ")
                date_naiss = input("Nouvelle date de naissance : ")
                classe = input("Nouvelle classe : ")
                gestion_etudiant.modifier_etudiant(id_, nom=nom, prenom=prenom, date_naissance=date_naiss, classe=classe)
            elif sous_choix == "4":
                gestion_etudiant.afficher_etudiants()

        elif choix == "2":
            print("\n-- Gestion des matières --")
            print("1. Ajouter matière")
            print("2. Afficher les matières")
            sous_choix = input("Choix : ")
            if sous_choix == "1":
                code = input("Code matière : ")
                nom = input("Nom matière : ")
                coeff = float(input("Coefficient : "))
                mat = Matiere(code, nom, coeff)
                gestion_matiere.ajouter_matiere(mat)
            elif sous_choix == "2":
                gestion_matiere.afficher_matieres()

        elif choix == "3":
            print("\n-- Saisie des notes --")
            id_ = input("ID Étudiant : ")
            code_mat = input("Code Matière : ")
            note = float(input("Note : "))
            date_eval = input("Date d'évaluation (YYYY-MM-DD) : ")
            note_obj = Note(id_, code_mat, note, date_eval)
            gestion_note.saisir_note(note_obj)

        elif choix == "4":
            print("\n-- Calcul des moyennes --")
            id_ = input("ID Étudiant : ")
            print("1. Moyenne dans une matière")
            print("2. Moyenne générale")
            sous_choix = input("Choix : ")
            if sous_choix == "1":
                code_mat = input("Code Matière : ")
                moyenne = gestion_note.calculer_moyenne_matiere(id_, code_mat)
                if moyenne is not None:
                    print(f"Moyenne de l'étudiant {id_} en {code_mat} : {moyenne}")
                else:
                    print("Aucune note trouvée.")
            elif sous_choix == "2":
                moyenne_gen = gestion_note.calculer_moyenne_generale(id_, gestion_matiere)
                if moyenne_gen is not None:
                    print(f"Moyenne générale : {moyenne_gen}")
                else:
                    print("Impossible de calculer la moyenne.")

        elif choix == "5":
            print("\n-- Affichage des bulletins --")
            id_ = input("ID Étudiant : ")
            gestion_note.afficher_bulletin(id_, gestion_matiere, gestion_etudiant)

        elif choix == "6":
            gestion_etudiant.sauvegarder()
            gestion_matiere.sauvegarder()
            gestion_note.sauvegarder()
            print("Données sauvegardées avec succès.")

        elif choix == "7":
            gestion_etudiant = GestionEtudiant()
            gestion_matiere = GestionMatiere()
            gestion_note = GestionNote()
            print("Données chargées.")

        elif choix == "8":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")
            
            
if __name__ == "__main__":
    menu_principal()

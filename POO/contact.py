class Contact:
    def __init__(self, nom, telephone, email):
        self.nom = nom
        self.telephone = telephone
        self.email = email
        
    def __str__(self):
        return f"{self.nom} -> {self.telephone} -> {self.email}"
    
class Annuaire:
    def __init__(self):
       self.contacts = {}
       
    def ajouterContact(self, contact):
        self.contacts[contact.nom] = contact
        
    def supprimerContact(self, nom):
        if nom in self.contacts:
            del self.contacts[nom]
            
    def rechercherContact(self, nom):
        contact = self.contacts.get(nom)
        if contact:
            print(contact)
            
    def afficherContact(self):
        for contact in self.contacts:
            print(contact)
            
            
c1 = Contact("Aïssata", "622000111", "aissata@mail.com")
c2 = Contact("Souleymane", "622000222", "souley@mail.com")

print(c1)

a = Annuaire()

a.ajouterContact(c1)
a.ajouterContact(c2)

print("Liste de contact")
a.afficherContact()

print("Apres suppresion de souleymane")
a.supprimerContact("Souleymane")
a.afficherContact()

print("Recherche de Aïssata")
a.rechercherContact("Aïssata")







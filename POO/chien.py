class Chien :
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
        
    def aboyer(self):
        
        print(f"Bonjour je suis {self.nom}, je suis un {self.race} et j'ai {self.age} ans. Tous les jours je fais Woof Woof!")
        

chienchien = Chien("chienchien", "chiwawa", 12)

chienchien.aboyer()
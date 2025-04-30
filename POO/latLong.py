class Lieu:
    def __init__(self, nom, coordonnees):
        self.nom = nom
        self.coordonnees = coordonnees  

    def distance_vers(self, autre_lieu):
        lat1, lon1 = self.coordonnees
        lat2, lon2 = autre_lieu.coordonnees
        return abs(lat1 - lat2) + abs(lon1 - lon2)  


lieu1 = Lieu("Paris", (48.8566, 2.3522))
lieu2 = Lieu("Londres", (51.5074, -0.1278))
lieu3 = Lieu("Madrid", (40.4168, -3.7038))

print(f"Distance Paris - Londres : {lieu1.distance_vers(lieu2):.2f}")
print(f"Distance Paris - Madrid : {lieu1.distance_vers(lieu3):.2f}")
print(f"Distance Londres - Madrid : {lieu2.distance_vers(lieu3):.2f}")

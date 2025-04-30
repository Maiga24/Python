class Gps:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
        
    def __str__(self):
        return (f'Latitude: {self.latitude}, longitude: {self.longitude}') 
    

coordonees = (
    Gps(23.43222, 234.980),
    Gps(23.43222, 234.980),
    Gps(23.43222, 234.980)
)

for coordonee in coordonees:
    print(coordonee)
# Exo 1

# ensemble = {"vache", "chien", "chat"}
# ensemble = set(["vache", "chien"])

# for element in ensemble :
#     print(element)

# Exo 2

# animaux1 = set(input("Donner un ensemble d'animaux separés avec espace : ").split())
# animaux2 = set(input("Donner un ensemble d'animaux dont un ou plusieurs du prenier ensemble : ").split())
 
# intersection = animaux1 & animaux2
# print(f"l'animal commun est : {intersection}")

# Exo 3

liste = [1,2,3,4,2,3,4]

sansDoublon = set(liste)

for element in sansDoublon :
    print(element)
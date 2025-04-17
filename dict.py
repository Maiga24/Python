# Exo 1

# dict = {
#     "nom": "maiga",
#     "age": 25,
#     "ville": "conakry"
#     }
# print(dict["nom"])
# print(dict["age"])
# print(dict["ville"])

# Exo 2

# notes = {
#     "math": 12,
#     "anglais": 15,
#     "francais": 16
# }

# moyenne = sum(notes.values()) / 3
# print(f'la moyenne est : {moyenne}')


# Exo 3 

dict = {}

n = int(input("Combien de paires clé-valeur voulez-vous saisir ? "))

for i in range(n):
    cle = input(f"Entrez la clé {i+1} : ")
    valeur = input(f"Entrez la valeur pour '{cle}' : ")
    dict[cle] = valeur  

print("\nVoici les paires clé-valeur saisies :")
for cle, valeur in dict.items():
    print(f"{cle} : {valeur}")
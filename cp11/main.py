import json

# charger les données depuis le fichier
with open('class.json','r') as file:
    eleves = json.load(file)


for eleve in eleves:
    print(eleve,eleves[eleve]['note'],eleves[eleve]['appreciation'])

# Sauvegarde de notre classe dans un fichier
with open("class.json","w+") as file:
    json.dump(eleves, file)



# ajouter un ou une élève
# eleves['Camille']['note'] = 20
# #del eleves['Camille']
#
# if 'Camille' in eleves.keys():
#     print("Camille est bien dans la classe")
# else:
#     print("Camille n'est pas dans la classe")
#
#  boucles qui va afficher le prénom et la moyenne
# for prenom,moyenne in eleves.items():
#     print(f"La moyenne de {prenom} est de {moyenne}/20")
# moyenne de la classe
# print (round(sum(eleves.values()) / len(eleves)))
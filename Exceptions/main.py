# while True:
#     try:
#         prixHt =  int(input("Entrer le prix hors taxe "))
#         prixTTC = prixHt + prixHt * 0.2
#         print(prixTTC)
#         break
#     except ValueError:
#         print("Attention tu dois mettre un nombre")
import json
from os.path import exists


class FileNotJsonFormatError(Exception):
    def __init__(self):
        self.message = "Vous ne pouvez mettre que des fichiers en .json"



def read_json_file(file_name):
    try:
        if not file_name.endswith('.json'):
            raise FileNotJsonFormatError
        fichier = open(file_name)
        print(json.load(fichier))
        fichier.close()
    except FileNotJsonFormatError as e:
        print(e.message)
    except (FileNotFoundError):
        print("Le fichier n'existe pas")
    # except (IndexError):
    #     print("La ligne que tu veux afficher n'existe pas")
    # finally:
    #     print("Fini")

read_json_file("bonjour.txt")